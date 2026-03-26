from dash import Input, Output
import plotly.express as px
import pandas as pd

# Charger les données
df = pd.read_csv("datas/avocado.csv")

def register_callbacks(app):

    @app.callback(
        Output("price-graph", "figure"),
        Input("region-dropdown", "value")
    )
    def update_graph(selected_region):
        # Filtrer les données
        filtered_df = df[df["region"] == selected_region]

        # Graphique
        fig = px.line(
            filtered_df,
            x="Date",
            y="AveragePrice",
            color="type",
            title=f"Prix des avocats - {selected_region}"
        )

        return fig