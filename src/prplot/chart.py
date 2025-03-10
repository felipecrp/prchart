from typing import List
import pandas as pd
import matplotlib.pyplot as plt

from prplot.plot import Plot
from prplot.style.chart_style import ChartStyle;

class Chart:
    def __init__(self, data: pd.DataFrame, binds, axes, label, style: ChartStyle, plots):
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
    
    def _draw(self):
        self._draw_axes()
        self._draw_plots()

    def _draw_axes(self):
        self.figure, self.ax = plt.subplots()
        ax = self.ax

        if 'title' in self.label:
            ax.set_title(self.label['title'])

        if 'x' in self.label:
            ax.set_xlabel(self.label['x'])
        else:
            ax.set_xlabel(self.binds['x'])

        if 'y' in self.label:
            ax.set_ylabel(self.label['y'])
        else:
            ax.set_ylabel(self.binds['y'])
        
        self.style.apply_to_axes(ax)
    
    def _draw_plots(self):
        for plot in self.plots:
            plot.fig = self.figure
            plot.ax = self.ax
            plot.draw()

    def save(self, filename):
        if not self.ax:
            self._draw()
        self.figure.savefig(filename)

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
    
    def style(self, style):
        self._style = style
        return self
    
    def build(self):
        return Chart(self._data, self._binds, self._axes, self._label, self._style, self._plots)

    def save(self, filename):
        chart = self.build()
        chart.save(filename)
        return chart

    def show(self):
        chart = self.build()
        chart.show()
        return chart

