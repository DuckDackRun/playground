import pandas as pd
import folium
from folium import GeoJson 

df_can = pd.read_csv("diebstahl_faelle.csv")

berlin_map = folium.Map(tiles="cartodb positron", location = (52.5162,13.3777),zoom_start= 10.5)

# GeoJson: Bezirke darstellen
bezirke_geo = r'./bezirksgrenzen.geojson'
file = open(bezirke_geo, encoding ="utf8")
text = file.read()

GeoJson(text).add_to(berlin_map) 

### Daten in Map darstellen
folium.Choropleth(
geo_data = bezirke_geo,
    data = df_can,
    columns = ("Gemeinde_name","Anzahl_Faelle"),
    key_on = 'feature.properties.Gemeinde_name',
    fill_color= 'Reds',
    nan_fill_color = "white",
    fill_opacity = 3,
    line_opacity = 0.1,
    name = 'Visualisierung',
    legend_name = 'Anzahl Farraddiebstähle'
    ).add_to(berlin_map)


style_function = lambda x: {'fillColor': '#ffffff', 
                            'color':'#000000', 
                            'fillOpacity': 0.1, 
                            'weight': 0.1}
highlight_function = lambda x: {'fillColor': '#000000', 
                                'color':'#000000', 
                                'fillOpacity': 0.50, 
                                'weight': 0.1}

#interaktive Gestaltung
df_can  = folium.features.GeoJson(
    bezirke_geo, 
    style_function = style_function,
    control = False,
    highlight_function = highlight_function,
    tooltip=folium.features.GeoJsonTooltip(
        fields=['Gemeinde_name','Gemeinde_schluessel'],
        aliases=['Bezirk','Bezirk-Schlüssel: '],
        style=("background-color: white; color: grey ;font-family: arial; font-size: 12px; padding: 10px;") ))

berlin_map.keep_in_front(df_can)
berlin_map.add_child(df_can)

### Map von Berlin wird ausgegeben
berlin_map.save("Berlin.html")
print("Hallo")