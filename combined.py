import pandas as pd
import plotly.express as px
import config
import numpy as np


DATA_FILENAME= config.paths_["DATA_FILENAME"]
WEIGHT_FILENAME= config.paths_["WEIGHT_FILENAME"]
filenames = [DATA_FILENAME, WEIGHT_FILENAME]


df1 = pd.read_csv(WEIGHT_FILENAME, names=["time", "weight"], header=None )
print(df1.head())

df2 = pd.read_csv(DATA_FILENAME, names=["time"] + [str(x) for x in list(np.arange(1,33))], header=None )


df = pd.concat([df1, df2])
print(df)
# fig = px.scatter(df, x="weight", y="4")
# fig.show()
# fig = px.scatter(df2.iloc[::100,:], x="time", y="4")
# fig.show()

df["weight"] = df["weight"].ffill()
# print (df.info())

# fig = px.scatter(df, x="weight", y="10")
# fig.show()

fig = px.scatter(df.iloc[::1,:])
fig.show()

fig = px.histogram(df.iloc[::1,:], x="weight")
fig.show()