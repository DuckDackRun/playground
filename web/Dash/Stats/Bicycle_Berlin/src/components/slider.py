from dash import Dash,html, dcc
from dash.dependencies import Input,Output
from .import ids
import pandas as pd

def render(app: Dash, data: pd.DataFrame):
    jahre =["2019","2020","2021","2022"]
    
    @app.callback( #callback, konstruktion
        Output(ids.BAR, "data"),
        Input(ids.SLIDER, "value"),
    )
    
    def selectthemall(value):
        return data #müsste man anpassen mit data[data.jahre=<value] 
    
    
    return html.Div(
        children=[
            html.H6("Jahre"),
            dcc.Slider(0,15,value=2020,
                        id=ids.SLIDER,    
                        marks={
                            0: {'label': '2019', 'style': {'color': '#77b0b1'}},
                            5: {'label': '2020', 'style': {'color': '#77b0b1'}},
                            10: {'label': '2021', 'style': {'color': '#77b0b1'}},
                            15: {'label': '2022', 'style': {'color': '#77b0b1'}}
            },
            included=False)
            ]
    )
    