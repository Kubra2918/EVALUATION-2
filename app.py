import dash
from dash import html
import dash_bootstrap_components as dbc
from pages import page1_cb
from pages import page2_cb
from pages import page3_cb


app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

page1_cb.register_callbacks(app)
page2_cb.register_callbacks(app)
page3_cb.register_callbacks(app)

server = app.server

# Navbar automatique
navbar = dbc.NavbarSimple(
    brand="Avocado Dashboard",
    children=[
        dbc.NavItem(
            dbc.NavLink(page["name"], href=page["path"])
        )
        for page in dash.page_registry.values()
    ],
)

app.layout = dbc.Container([
    navbar,
    dash.page_container
], fluid=True)

if __name__ == "__main__":
    app.run(debug=True)