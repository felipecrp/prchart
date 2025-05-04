import pytest

import pandas as pd


@pytest.fixture
def dataset_1():
    data = [
        { 
            "cat": v[0],
            "v1": v[1],
            "v2": v[2]
        } for v in [
            ("p1", 1, 6),
            ("p2", 2, 5),
            ("p2", 3, 4),
            ("p3", 4, 3),
            ("p3", 5, 2),
            ("p3", 6, 1)
        ]
    ]
    data = pd.DataFrame(data)
    return data


@pytest.fixture
def iris():
    data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/iris.csv')
    return data
