import folium
import Map

icon = folium.Icon(color='darkpurple', icon='paperclip')
popup_html = f'<a href="http://127.0.0.1:5000/events/">Мероприятия</a>'
marker = folium.Marker(location=Map.orel, icon=icon, popup=folium.Popup(popup_html, max_width=300))

events = folium.FeatureGroup(name='Мероприятия', show=False).add_to(Map.orel_map)
