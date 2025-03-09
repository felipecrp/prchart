import pandas as pd;

class Chart:
    def __init__(self, data: pd.DataFrame, binds, axes, plots):
        self.data = data
        self.binds = binds
        self.axes = axes
        self.plots = plots
        for plot in self.plots:
            plot.chart = self
        
    def show(self):
        for plot in self.plots:
            plot.show()
