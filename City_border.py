import folium
from Map import orel_map

limit_menu = folium.FeatureGroup(name='Граница города', show=False).add_to(orel_map)

# Добавляем на карту границы города Орла из GeoJSON-файла
limit = folium.GeoJson(
    'orel.geojson',
    name='orel',
    style_function=lambda feature: {
        'fillColor': 'white',
        'color': 'grey',
        'weight': 2.5,
        'fillOpacity': 0.01,
    }
)