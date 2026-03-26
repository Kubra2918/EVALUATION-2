import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

dash.register_page(__name__, path="/", name="Page 1")

df = pd.read_csv("datas/avocado.csv")

regions_fixed = ["MidSouth", "Northeast", "SouthCentral", "Southeast", "TotalUS", "West"]

df_fixed = df[df["region"].isin(regions_fixed)]

fig_fixed = px.line(
    df_fixed,
    x="Date",
    y="Total Volume",
    color="region",
    title="Volumes totaux - régions principales"
)
regions = df["region"].unique()

layout = html.Div([

    html.H1(
    "Quantités vendues (Total Volume)",
    style={
        "backgroundColor": "#3b8dbd",
        "color": "white",
        "padding": "10px",
        "borderRadius": "5px",
        "marginBottom": "15px"
    }
),
    
    html.Div([

        html.Div([
            dcc.Graph(figure=fig_fixed)
        ], className="card", style={"width": "48%"}),

        html.Div([
            html.Label("Sélectionnez une région:"),
            dcc.Dropdown(
                id="region-dropdown",
                options=[{"label": r, "value": r} for r in regions],
                value=regions[0]
            ),
            dcc.Graph(id="price-graph")
        ], className="card", style={"width": "48%"})

    ], style={"display": "flex", "justify-content": "space-between"})
])