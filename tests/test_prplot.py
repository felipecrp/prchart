
import pandas as pd
import prplot as pr

def test_chart():
    data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv')
    pr.chart(
        data=data,
        binds={
            'category': 'Embarked',
        },
        axes=None,
        plots=[
            pr.plot.bar()
        ]
    )
