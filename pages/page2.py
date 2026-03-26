import dash
from dash import html, dash_table, dcc
import pandas as pd

dash.register_page(__name__, path="/page2", name="Page 2")

df = pd.read_csv("datas/avocado.csv")

regions = df["region"].unique()
types = df["type"].unique()

layout = html.Div([
    html.H1("Page 2- Tableau des données"),

    dcc.Dropdown(
        id="region-filter",
        options=[{"label": r, "value": r} for r in regions],
        placeholder= "Choisir une region"
    ),
    dcc.Dropdown(
       id= "type-filter",
         options=[{"label": t, "value": t} for t in types],
         placeholder= "Choisir un type"
    ),

    dash_table.DataTable(
       id="table",
       columns=[{"name": i, "id": i} for i in df.columns],
       data=df.head(20).to_dict("records"),
       page_size=10 
    )
])