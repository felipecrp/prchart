
import pandas as pd
import prplot as pr

def test_chart():
    iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    pr.chart(
        data=iris,
        binds=pr.bind(
            x='petal_width',
            y='petal_length'
        ),
        plots=[
            pr.plot.bar()
        ]
    )

