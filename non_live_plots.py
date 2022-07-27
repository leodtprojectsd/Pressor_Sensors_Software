"""
Include all non-live plots, post processing.

"""

import plotly.express as px
import pandas as pd
import config

col_names = ["time"] + [str(x) for x in range(1, 32+ 1)]
df = pd.read_csv(config.paths_["DATA_FILENAME"], names=col_names, header=None)

df = df[(df > 0).all(1)]
df = df[(df < 50e6).all(1)]
df.iloc[:, 1:] = df.iloc[:, 1:].rolling(30, min_periods=1).mean()

fig = px.line(df.iloc[::20, :], x="time", y=col_names[1:])
fig.show()