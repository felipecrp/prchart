
import pandas as pd

import prplot.plot

from .bind import Bind
from .chart import Chart


def chart(data: pd.DataFrame, binds, plots):
    chart = Chart(data, binds, plots)
    chart.show()


def bind(*args, **kwargs):
    bind = Bind(kwargs)
    return bind

