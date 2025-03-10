
import pandas as pd
import prplot as prp


def test_chart_bar():
    data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv')
    style = prp.style.Grayscale()
    (prp.chart()
        .data(data)
        .bind(
            x='Embarked',
        )
        .style(style)
        .label(
            title='Embarked Count',
            x='Embarked?',
            y='People Count'
        )
        .plot(prp.plot.Bar())
        .save('bar.png')
        .show()
    )


def test_chart_scatter():
    data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv')
    style = prp.style.Grayscale()
    (prp.chart()
        .data(data)
        .bind(
            x='Age',
            y='Fare'
        )
        .style(style)
        .plot(prp.plot.Scatter())
        .save('scatter.png')
        .show()
    )

def test_chart_boxplot():
    style = prp.style.Grayscale()
    data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv')
    (prp.chart()
        .data(data)
        .bind(
            x='Sex',
            y='Fare'
        )
        .plot(prp.plot.BoxPlot())
        .style(style)
        .save('boxplot.png')
        .show()
    )