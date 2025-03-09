import pandas as pd;

class Chart:
    def __init__(self, data: pd.DataFrame, binds, axes, style, plots):
        self.data = data
        self.binds = binds
        self.axes = axes
        self.style = style
        self.plots = plots
        for plot in self.plots:
            plot.chart = self

    def save(self, filename):
        for plot in self.plots:
            plot.save(filename)

    def show(self):
        for plot in self.plots:
            plot.show()

class ChartBuilder:
    def __init__(self):
        self._data = None
        self._binds = {}
        self._axes = None
        self._plots = []
        self._style = None
        
    def data(self, data: pd.DataFrame):
        self._data = data
        return self
    
    def bind(self, **kwargs):
        self._binds.update(kwargs)
        return self
    
    def plot(self, plot):
        self._plots.append(plot)
        return self
    
    def style(self, style):
        self._style = style
        return self
    
    def build(self):
        return Chart(self._data, self._binds, self._axes, self._style, self._plots)

    def save(self, filename):
        chart = self.build()
        chart.save(filename)
        return chart

    def show(self):
        chart = self.build()
        chart.show()
        return chart

