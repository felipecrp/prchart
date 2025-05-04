import pandas as pd

from prchart.bind import Category, Value

from .fixtures.dataset import iris 


class DescribeCategory:
    def it_has_values(self, iris: pd.DataFrame):
        category = Category("species")
        category.setup(iris)
        series = category.values()
        assert "setosa" in series
        assert "versicolor" in series
        assert "virginica" in series
    

class DescribeValue:
    def it_has_values(self, iris: pd.DataFrame):
        value = Value("sepal_length")
        value.setup(iris)
        series = value.values()
        assert 5.1 == series[0]
