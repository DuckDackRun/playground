
import webbrowser
import psycopg2
import psycopg2.extras
from src.components import bez_dropdown,bar_chart,pie_chart,slider,ids
from dash import Dash, html, dcc
#from dash_bootstrap_components.theme import BOOTSTRAP
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from dash.dependencies import Input, Output
import webbrowser


conn=None
try:
    conn=psycopg2.connect(host ="postgres.tut.jbb.ghsq.de", dbname = "gruppe1", user = "gruppe1", password = "peirieBei4Aeb9sae4neThiSangechee")

    cur= conn.cursor(cursor_factory=psycopg2.extras.DictCursor) #<- sorgt dafür, dass data mittels [attribut] zugreifbar ist


    #####wichtiger code ######################################
    
    '''
    cur.execute("SELECT * FROM bezirksgrenzen;") 
    dt=cur.fetchall()
    bezirke=list(df.columns.values)

    column_names =["Id","Bezirk","Gestohlen","Gender"]  #muss man manuell selber machen?
    data=pd.DataFrame(dt,columns=column_names)
    
    
    
    
    '''    
    


    cur.execute("SELECT * FROM Stat;") 
    dt=cur.fetchall()

    column_names =["Id","Bezirke","Anzahl gestohlener Fahrräder","Gender"]  #muss man manuell selber machen?
    data=pd.DataFrame(dt,columns=column_names)
    #objekt erstellen mit diesem eigenschaften
    
    
    cur.execute("SELECT * FROM StatJahr;") 
    dt=cur.fetchall()

    column_names =["Id","Jahr","Anzahl gestohlener Fahrräder","wtf"]  #muss man manuell selber machen?
    data1=pd.DataFrame(dt,columns=column_names)

    conn.commit()#muss ich wa nicht machen
    
except Exception as error:
  print("error, mein leben ist schlimm", error)
  data=[]
finally:
  if conn is not None:
    conn.close()

#def main()->None:
  
#mittels postgres fetchen
print(data)


app=Dash(__name__)
app.title="Bycyle-Crime Dashboard"
app.layout =html.Div(
    children=[html.Div(children=[
        html.P(children="🚲",className="header-emoji"),
        html.H1(children="Radstatistiken",className="header-title"),#definieren ein css file, recyclbar, skalierbar
        html.Hr(),
        html.P(
            children=(
                "Analyze the number of stolen bikes in Berlin"),className="header-description"
            )
      ],className="header"),
      html.Div(children=[bez_dropdown.render(app,data),html.Hr()]),
      html.Div(children=[bar_chart.render(app,data),]),     
      html.Div(children=[dcc.Graph(
          figure={
              "data": [
                  {
                      "x": data1["Jahr"],  #statt jahr weisen wir jedem jahr,monat,tag einer id zu
                      "y": data1["Anzahl gestohlener Fahrräder"], #müssen auf echte Daten angepasst werden /column namen
                      "type": "lines",
                  },
              ],
              "layout": {"title": "Absolute Zahl an gestohlenen Rädern"},
          },
      )],className="card"),
      html.Div(children=[slider.render(app,data),]),
      html.Div(children=[dcc.Graph(figure=px.bar(data, x="Bezirke", y="Anzahl gestohlener Fahrräder", title="Gestohlene Fahrräder"))]),
      #piechart
      
      html.Div([
      html.H4('Prozentuale Übersicht mittels Kuchendiagramm (falls es nicht streikt)'),
      dcc.Graph(id="piechart"),
      html.P("Names:"),
      dcc.Dropdown(id='Bezirke',
        options=['Reinickendorf','Steglitz','Ufer','Lol'],
        value='Steglitz', clearable=False
      ),
      html.P("Values:"),
      dcc.Dropdown(id='values',
        options=['Damenfahrrad', 'Herrenfahrrad', 'Mountainbike'],
        value='Mountainbike', clearable=False
      ),
      ]),
      #html.Div(children=[pie_chart.render(app, data),]),
      html.H6(children="Bemerkung: Alle hier zufindenen Daten sind von mir ausgedacht (außer die Daten der Kartenvisualisierung), das Einbeziehen der richtigen Daten braucht mehr Zeit",className="headertitle"),
      html.Iframe(srcDoc=open("Berlin.html","r").read(),height="1067px",width="90%",className="body")
      ])
    
    
@app.callback(
    Output("piechart", "figure"), 
    [Input("Bezirke", "value"), 
    Input("values", "value")])

def generate_chart(names, values):
    #df = px.data.tips() # replace with your own data source
    #fig = px.pie(data, values=values, names=names, hole=.3)
    #return fig
    '''
    pie = go.Pie(
    labels=data["Bezirke"].tolist(),
    values=data["Gestohlen"].tolist(),
    hole=0.5
    )'''

    fig = px.pie(data,values="Bezirke",names="Anzahl gestohlener Fahrräder")#go.Figure(data=[pie])
   
    return fig


  
if __name__ =="__main__":
  webbrowser.open('http://127.0.0.1:8050/',new=0,autoraise=True)
  app.run_server(debug=True)


