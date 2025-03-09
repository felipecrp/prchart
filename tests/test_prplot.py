
import pandas as pd
import prplot as prp


def test_chart_bar():
    data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv')
    (prp.chart()
        .data(data)
        .bind(
            category='Embarked',
        )
        .plot(prp.plot.Bar())
        .show()
    )


def test_chart_scatter():
    data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv')
    (prp.chart()
        .data(data)
        .bind(
            x='Age',
            y='Fare'
        )
        .plot(prp.plot.Scatter())
        .show()
    )