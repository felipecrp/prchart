import pandas as pd;

class Chart:
    def __init__(self, data: pd.DataFrame, binds, plots):
        self.data = data
        self.binds = binds
        self.plots = plots
        
    def show(self):
        pass