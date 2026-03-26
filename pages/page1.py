import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

dash.register_page(__name__, path="/", name="Page 1")

df = pd.read_csv("datas/avocado.csv")

fig = px.line(df, x="Date", y="AveragePrice", title="Prix moyen des avocats")

layout = html.Div([
    html.H1("Page 1- Analyse des prix"),
    dcc.Graph(figure=fig)
])