import pandas as pd

import plotly.express as px

#reading data from csv files
df = pd.read_csv("data.csv")
fig = px.bar(df, x='Date', y='Number Of Cases')
fig.show()
