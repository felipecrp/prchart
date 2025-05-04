"""
Draw the chart geometry
"""
from typing import List
import pandas as pd

from prchart.bind import Category, Series

class Geometry:
    def __init__(self, series: List[Series]):
        self.series = series
        
    def setup(self, series: List[Series]):
        self.series = series

    def series_by_type(self, type, pos: int):
        count = 0
        for s in self.series:
            if isinstance(s, type):
                if count == pos:
                    return s
                else:
                    count += 1
        # throw exception



class Bar(Geometry):
    """
    Draw a bar plot
    """
    def __init__(self, series: List[Series] = None):
        super().__init__(series)

    def draw(self, ax):
        categories = self.series_by_type(Category, 0).values()
        values = []
        ax.bar(
            categories, 
            values, 
        )
