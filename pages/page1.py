import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

dash.register_page(__name__, path="/", name="Page 1")

df = pd.read_csv("datas/avocado.csv")

regions = df["region"].unique()



layout = html.Div([
    html.H1("Page 1- Analyse des prix"),

    dcc.Dropdown(
        id="region-dropdown",
        options=[{"label": r, "value": r} for r in regions],
        value=regions[0]
    ),
    dcc.Graph(id="price-graph")

])