"""
Publish Ready Chart


import prchart as pr
import prchart.bind as bind
import prchart.chart as chart


```
(pr
    .data(
        dataframe,
        bind.Category(),
        bind.Value()
    )
    .plot(
        chart.Bar()
    )
)
```

"""
import pandas as pd

from .chart import BindChart

import prchart.plot
import prchart.style

from .chart import Chart, ChartBuilder



def data(df: pd.DataFrame, *binds):
    return BindChart(df, binds) 


def chart():
    return ChartBuilder()
