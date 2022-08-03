"""
Include all non-live plots, post processing.

"""

import plotly.express as px
import pandas as pd
import config

col_names = ["time"] + [str(x) for x in range(1, 32+ 1)]
df = pd.read_csv(config.paths_["DATA_FILENAME"], names=col_names, header=None)

# df = df[(df > 0).all(1)]
# df = df[(df < 50e6).all(1)]
# df.iloc[:, 1:] = df.iloc[:, 1:].rolling(30, min_periods=1).mean()
df["time"] = df["time"] - df["time"].iloc[0]
print (col_names[1:])
fig = px.line(df.iloc[::50, :], x="time", y=col_names[1:])
fig.update_layout(
    title="Pins that work - tested all with R=10Mohm",
    xaxis_title="Time[S]",
    yaxis_title="R [OHM]",
    legend_title="PIN",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    )
)
# fig.show()
fig.write_html(r"C:\Users\leodavide.torchia2\Desktop\this.html")
print ("done")