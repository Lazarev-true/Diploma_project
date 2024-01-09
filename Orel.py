import requests
import folium
import Information
import City_border
import Map
import Events
from Places_city import place
from flask import Flask

app = Flask(__name__)

@app.route('/events/')
def get_data():
    return requests.get('https://zeroevent.ru/city/105').content

places = place()

City_border.limit_menu.add_child(City_border.limit)
Information.information.add_child(folium.Marker(Map.orel, icon=Information.icon, popup=Information.information_popup))
Events.events.add_child(Events.marker)

folium.LayerControl(collapsed=False).add_to(Map.orel_map)

Map.orel_map.save('orel.html')

if __name__ == '__main__':
    app.run()