
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd

from . import ids
#anderes dataset wählen?


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.BAR, "children"),
        Input(ids.BEZ, "value")
        
    )
    def update(bezirke: list[str]) -> html.Div:
        filtered_data = px.data.query("Bezirk in @bezirke")

        #if filtered_data.shape[0] == 0:
        #    return html.Div("No data selected.", id=ids.BAR)

        fig = px.bar(filtered_data, x="Bezirke", y="Gestohlen", title="Gestohlene Fahrräder")
        fig.update_traces(textfont_size=12,textangle=0,textposition="outside",cliponaxis=False)
        return html.Div(dcc.Graph(figure=fig), id=ids.BAR)

    return html.Div(id=ids.BAR)