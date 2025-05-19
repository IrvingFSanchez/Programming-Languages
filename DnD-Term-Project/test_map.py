import folium
print("Folium version:", folium.__version__)
m = folium.Map(location=[41.8781, -87.6298])
m.save("test.html")
print("Map generated! Open test.html")