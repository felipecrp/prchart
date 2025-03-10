
import pandas as pd
import prplot as prc


def test_chart_bar():
    data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv')
    style = prc.style.Grayscale()
    (prc.chart()
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
        .plot(prc.plot.Bar())
        .size(
            width=4,
            height=3
        )
        .save('bar.png', dpi=300)
        .show()
    )


def test_chart_scatter():
    data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv')
    style = prc.style.Grayscale()
    (prc.chart()
        .data(data)
        .bind(
            x='Age',
            y='Fare'
        )
        .style(style)
        .plot(prc.plot.Scatter())
        .save('scatter.png')
        .show()
    )

def test_chart_boxplot():
    style = prc.style.Grayscale()
    data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv')
    (prc.chart()
        .data(data)
        .bind(
            x='Sex',
            y='Fare'
        )
        .plot(prc.plot.BoxPlot())
        .style(style)
        .save('boxplot.png')
        .show()
    )