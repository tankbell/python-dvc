# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import pandas as pd

iris = pd.read_csv(
    "../data/iris.data",
)

iris.columns = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
    "class",
]

iris_virginica = iris[
    iris["class"] == "Iris-virginica"
]

assert len(iris_virginica) == 50

iris_virginica.to_csv(
    "../interim/virginica.csv",
    index=False,
)


