from dash import Input, Output
import pandas as pd

df = pd.read_csv("datas/avocado.csv")

def register_callbacks(app):

    @app.callback(
        Output("table", "data"),
        Input("region-filter", "value"),
        Input("type-filter", "value")
    )
    def update_table(selected_region, selected_type):

        filtered_df = df

        if selected_region:
            filtered_df = filtered_df[filtered_df["region"] == selected_region]

        if selected_type:
            filtered_df = filtered_df[filtered_df["type"] == selected_type]

        return filtered_df.to_dict("records")