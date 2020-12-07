import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
fig = px.scatter(df, x="Date", y="Number Of Cases",
	          size="Percentage",color="Country",
                   size_max=60)
fig.show()
