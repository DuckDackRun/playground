from dash import Dash,html, dcc
from . import bar_chart,bez_dropdown

def createlayout(app: Dash,data)->html.Div:
    return html.Div(children=[#hier wird er cod in html code umtransformiert
      html.H1(children="Radstitiken",className="headertitle"),#definieren ein css file, recyclbar, skalierbar
      
      html.P(children=( "Analyze the number of stolen bikes"),
      ),
      dcc.Graph(
          figure={
              "data": [
                  {
                      "x": data["Bezirk"],
                      "y": data["AdgR"],
                      "type": "lines",
                  },
              ],
              "layout": {"title": "Absolute Zahl an gestohlenen Rädern"},
          },
      ),dcc.Graph(
          figure={
              "data": [
                  {
                      "x": data["Bezirk"],
                      "y": data["AdgR"],
                      "type": "lines",
                  },
              ],
              "layout": {"title": "Relative Zahl an gestohlenen Rädern"},
          },
      ),html.Div(
                className="dropdown-container",
                children=[
                    bez_dropdown.render(app),
                ],
            ),
            bar_chart.render(app),
        ])