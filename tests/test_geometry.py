import pandas as pd
from pytest_mock import class_mocker, mocker

from prchart.geometry import Bar

from .fixtures.dataset import dataset_1
from prchart.bind import Category, Value


class DescribeBarChart:
    def it_plot(self, mocker, dataset_1):
        category = Category("cat")
        category.setup(dataset_1)
        bar = Bar()
        bar.setup([category])
        
        ax_mock = mocker.MagicMock()
        bar.draw(ax_mock)

        ax_mock.bar.assert_called_once()
        args, kwargs = ax_mock.bar.call_args
        assert args[0].tolist() == ["p1", "p2", "p2", "p3", "p3", "p3"]
        assert args[1] == []

         