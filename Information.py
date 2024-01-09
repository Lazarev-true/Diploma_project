import folium
import wikipedia
from Map import orel_map

city = 'город Орёл'

information = folium.FeatureGroup(name='О городе', show=False).add_to(orel_map)
wikipedia.set_lang('ru')
information_city = wikipedia.page(city).summary
information_popup = folium.Popup(information_city, max_width=300) # Значение отображения информации по клику на маркер
icon = folium.Icon(color='gray', icon='fullscreen')         # Иконки маркера и красного цвета
