from typing import List
import pandas as pd
import matplotlib.pyplot as plt

from prchart.bind import Series
from prchart.geometry import Geometry
from prchart.plot import Plot
from prchart.style.chart_style import ChartStyle;


class BindChart:
    def __init__(self, data: pd.DataFrame, series: List[Series]):
        self.data = data
        self.serie = series

    def geometry(self, *geometries):
        return GeometryChart(self.data, self.series, geometries)


class GeometryChart:
    def __init__(self, data: pd.DataFrame, series: List[Series], geometries: List[Geometry]):
        self.data = data
        self.serie = series
        self.geometries = geometries
    
    def plot(self):
        return self
    
    def save(self):
        return self


class Chart:
    def __init__(self, data: pd.DataFrame, size, binds, axes, label, style: ChartStyle, plots):
        self.data = data
        self.binds = binds
        self.axes = axes
        self.style = style
        self.plots: List[Plot] = plots
        self.label = label
        for plot in self.plots:
            plot.chart = self
        self.figure = None
        self.ax = None
        self.size = size
    
    def _draw(self):
        self._draw_figure()
        self._draw_axes()
        self._draw_plots()

    def _draw_figure(self):
        if self.size:
            self.figure, self.ax = plt.subplots(figsize=(self.size['width'], self.size['height']))
        else:
            self.figure, self.ax = plt.subplots()
        
        fig = self.figure
        self.style.apply_to_figure(fig)

    def _draw_axes(self):
        ax = self.ax

        if 'title' in self.label:
            ax.set_title(
                self.label['title'], 
                loc=self.style.style['title']['position'], 
                color=self.style.style['title']['color'], 
                fontsize=self.style.style['title']['fontsize'], 
                fontweight=self.style.style['title']['fontweight'], 
                fontname=self.style.style['title']['fontname']
            )

        if 'x' in self.label:
            ax.set_xlabel(self.label['x'])
        elif 'x' in self.binds:
            ax.set_xlabel(self.binds['x'])

        if 'y' in self.label:
            ax.set_ylabel(self.label['y'])
        elif 'y' in self.binds:
            ax.set_ylabel(self.binds['y'])
        
        self.style.apply_to_axes(ax)
    
    def _draw_plots(self):
        for plot in self.plots:
            plot.fig = self.figure
            plot.ax = self.ax
            plot.draw()

    def save(self, filename, dpi=96):
        if not self.ax:
            self._draw()
        self.figure.savefig(filename, dpi=dpi)

    def show(self):
        if not self.ax:
            self._draw()
        plt.show()


class ChartBuilder:
    def __init__(self):
        self._data = None
        self._binds = {}
        self._axes = None
        self._plots = []
        self._style = None
        self._label = {}
        self._size = None
        
    def data(self, data: pd.DataFrame):
        self._data = data
        return self
    
    def bind(self, **kwargs):
        self._binds.update(kwargs)
        return self
    
    def label(self, **kwargs):
        self._label.update(kwargs)
        return self

    def plot(self, plot):
        self._plots.append(plot)
        return self
    
    def size(self, width, height):
        self._size = {
            'width': width,
            'height': height
        }
        return self
    
    def style(self, style):
        self._style = style
        return self
    
    def build(self) -> Chart:
        return Chart(self._data, self._size, self._binds, self._axes, self._label, self._style, self._plots)

    def save(self, filename, dpi=96) -> Chart:
        chart = self.build()
        chart.save(filename, dpi)
        return chart

    def show(self) -> Chart:
        chart = self.build()
        chart.show()
        return chart

