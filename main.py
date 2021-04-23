import pandas as pd
import csv
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv("data.csv")


print(df.groupby('level')["attempt"].mean())

fig = px.scatter(x = df.groupby('level')["attempt"].mean() , y="level-1" , orientation='h')
fig.show()
