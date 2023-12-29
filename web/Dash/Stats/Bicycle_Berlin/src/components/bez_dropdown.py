from dash import Dash,html, dcc
from dash.dependencies import Input,Output
from . import ids
import pandas as pd

def render(app: Dash, data: pd.DataFrame):
    bezirke =["Reinickendorf","Teglitz","Saarhausen","Mzahn"]
    gender=["Dame","Herr"]
    #plan für die zukunft eine datei data mit schema , welche man importen könnte
    
    
    @app.callback( #callback, konstruktion
        Output(ids.BEZ, "value"),
        Input(ids.BUTTON, "n_clicks"),
    )
    
    def selectthemall(_:int)->list[str]:
        return bezirke
    
    @app.callback(
        Output(ids.DROPGENDER, "value"),
        Input(ids.BUTGENDER, "n_clicks"),
    )
    
    def selectall(_:int)->list[str]:
        return gender
    
    return html.Div(
        children=[
            html.H6("Bezirk"),
            dcc.Dropdown(
                id=ids.BEZ,
                options=[{"label": bez, "value":bez} for bez in bezirke],
                value=bezirke,
                multi=True, clearable=False,
                className="dropdown"  
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.BUTTON,
                n_clicks=0,
            ),html.H6("Gender"),
            dcc.Dropdown(
                id=ids.DROPGENDER,
                options=[{"label": gend, "value":gend} for gend in gender],
                value=gender,
                multi=True,clearable=False,
                className="dropdown"   
            ),
            html.Button(
                className="dropdown-button",
                children=["Alle Geschlechter"],
                id=ids.BUTGENDER,
                n_clicks=0,
            )
            ]
    )
    