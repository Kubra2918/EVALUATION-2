import dash
from dash import html, dash_table
import pandas as pd

dash.register_page(__name__, path="/page2", name="Page 2")

df = pd.read_csv("datas/avocado.csv")

layout = html.Div([
    html.H1("Page 2- Tableau des données"),

    dash_table.DataTable(
       id= "table",
       columns=[{"name": i, "id": i} for i in df.columns],
       data=df.head(20).to_dict("records"),
       page_size=10 
    )
])