"""
Map the dataframe columns to the chart data series
"""
import pandas as pd


class Series:
    """
    A generic chart data serie
    """
    def __init__(self, column: str):
        super().__init__()
        self.column = column
        self.data = None

    def setup(self, data: pd.DataFrame):
        self.data = data

    def values(self):
        return self.data[self.column].values


class Category(Series):
    """
    A category serie that may be used to group values 
    """
    def __init__(self, column: str):
        super().__init__(column)

    def values(self):
        data = self.data.groupby([self.column]).size().reset_index(name='count')
        return data[self.column].values


class Value(Series):
    """
    A simple serie
    """
    def __init__(self, column: str):
        super().__init__(column)

