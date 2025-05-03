"""
Map the dataframe columns to the chart data series
"""
import pandas as pd


class Serie:
    """
    A generic chart data serie
    """
    def __init__(self, column: str):
        super().__init__()
        self.column = column

    def data(self, df: pd.DataFrame):
        return df[self.column]


class Category(Serie):
    """
    A category serie that may be used to group values 
    """
    def __init__(self, column: str):
        super().__init__(column)


class Value(Serie):
    """
    A simple serie
    """
    def __init__(self, column: str):
        super().__init__(column)

