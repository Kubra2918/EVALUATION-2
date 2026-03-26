import dash
from dash import html, dcc

dash.register_page(__name__, path="/page3", name="Page 3")

layout = html.Div([
   html.H1("Page 3 - Explications markdown", style={"color": "white"}),

    html.Div([

        dcc.Tabs(
            id="tabs-markdown",
            value="tab-1",
            children=[
                dcc.Tab(label="Accueil", value="tab-1"),
                dcc.Tab(label="Layout", value="tab-2"),
                dcc.Tab(label="Callback", value="tab-3"),
            ]
        ),

        html.Div(id="markdown-content")

    ], className="card")

])
