import dash
from dash import html, dcc

dash.register_page(__name__, path="/page3", name="Page 3")

layout = html.Div([
    html.H1("Page 3 - Explications markdown"),

    dcc.Tabs(
        id="tabs-markdown",
        value = "tab1",
        children=[
            dcc.Tab(label="Expli 1", value="tab-1"),
            dcc.Tab(label="Expli 2", value="tab-2"),
            dcc.Tab(label="Expli 3", value="tab-3"),
        ]

    ),

    html.Div(id="markdown-content")
])
