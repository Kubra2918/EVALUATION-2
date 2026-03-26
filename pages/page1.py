import dash
from dash import html

dash.register_page(__name__, path="/", name="Page 1")

layout = html.Div("Page 1")