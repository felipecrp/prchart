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

import prchart.plot
import prchart.style

from .chart import Chart, ChartBuilder


def chart():
    return ChartBuilder()
