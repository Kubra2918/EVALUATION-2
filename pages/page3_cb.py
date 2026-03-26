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
            return dcc.Markdown(md1)
        elif tab == "tab-2":
            return dcc.Markdown(md2)
        else:
            return dcc.Markdown(md3)