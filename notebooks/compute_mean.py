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

virginica = pd.read_csv(
    "../interim/virginica.csv",
)

virginica

mean_data = virginica.mean(axis = 0).reset_index()

mean_data.to_csv("../outputs/mean_data.csv", index=False)


