import dash
from dash import html, dcc, Input, Output, callback
import plotly.express as px

app = dash.Dash(
    __name__,
    meta_tags=[{
        "name": "viewport",
        "content": "width=device-width, initial-scale=1"
    }]
)

@callback(Output("time-series", "figure"), Input("slider", "value"))
def plot_data(vals):

    x = ["2025-07-10", "2025-07-12", "2025-07-14", "2025-07-16", "2025-07-24"]
    y = [10, 20, 30, 40, 20]
    fig = px.scatter(
        x=x[vals[0]:vals[1]],
        y=y[vals[0]:vals[1]],
    )
    return fig

app.layout = html.Div(
    [
        # graph
        dcc.Graph(id='time-series'),
        dcc.RangeSlider(min=0, max=5, step=1, value=[0, 5], id="slider")
        # slider
    ]
)

app.run('localhost', debug=True)

