import folium
map_osm = folium.Map(location=[55.704126,12.57485],
                   zoom_start=14)
folium.Marker([55.704126,12.57485], popup='Østerbro har fået en ny midlertidig urbanhavn på bunkeren på Carl Nielsen Allé').add_to(map_osm)
map_osm