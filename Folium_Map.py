import folium
import pandas as pd
# Import our data
data = pd.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
# Create coloring function
def get_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
# Create a map object
map = folium.Map(location=[39.031942, -105.904693], tiles="Stamen Terrain", zoom_start=4)
# Create a features group
fg = folium.FeatureGroup(name="My Map")
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el) + "m", icon=folium.Icon(color=get_color(el))))
fg.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read()))
map.add_child(fg)
# Save the map
map.save("map.html")