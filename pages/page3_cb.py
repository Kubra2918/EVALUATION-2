from dash import Input, Output, dcc

def read_markdown_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

md1 = read_markdown_file("expli1.md")
md2 = read_markdown_file("expli2.md")
md3 = read_markdown_file("expli3.md")

def register_callbacks(app):

    @app.callback(
        Output("markdown-content", "children"),
        Input("tabs-markdown", "value")
    )
    def render_markdown(tab):
        if tab == "tab-1":
            return dcc.Markdown(md1, style={"padding": "20px", "color":"white", "backgroundColor": "#1e1e1e"})
        elif tab == "tab-2":
            return dcc.Markdown(md2, style={"padding": "20px", "color":"white", "backgroundColor": "#1e1e1e"})
        else:
            return dcc.Markdown(md3, style={"padding": "20px", "color":"white", "backgroundColor": "#1e1e1e"})