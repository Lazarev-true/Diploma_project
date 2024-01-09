import folium
import requests
from Map import orel_map
from Picture import get_image_url

def place():
    for points, value in points_all.items():
        for point in points:
            # отправляем запрос к API 2GIS для поиска координат
            response = requests.get(f'https://catalog.api.2gis.com/3.0/items?q={point}&key={api_key}&fields=items.geometry.centroid')
            # проверяем статус код ответа
            if response.status_code == 200:
                # извлекаем координаты из ответа
                try:
                    coordinates_string = response.json()['result']['items'][0]['geometry']['centroid']
                    # преобразуем строку координат в пару чисел
                    coordinates = tuple(reversed(list(map(float, coordinates_string.strip('POINT()').split()))))
                    # Получаем ссылку на изображение
                    image_url = get_image_url(point)

                    icon = folium.Icon(color=value[0], icon=value[1])

                    # Создаем маркер с подсказкой, содержащей изображение
                    marker = folium.Marker(coordinates, icon=icon, popup=folium.Popup(f"{point}\n<img src='{image_url}'>", max_width=170))
                    value[2].add_child(marker)
                except KeyError:
                    print('Координаты не найдены')
    return value[2]

api_key = '4ae14aed-2edd-46c3-b914-90b516b99f04'

train_group = folium.FeatureGroup(name='Места для прогулок', show=False).add_to(orel_map)
photo_group = folium.FeatureGroup(name='Где сфотографироваться', show=False).add_to(orel_map)
monument_group = folium.FeatureGroup(name='Памятники города', show=False).add_to(orel_map)

points_all = {('Орел, Детский парк',
               'Орел, Парк Победы',
               'Орел, Разградский парк'): ('red','asterisk', train_group), 
              ('Орел, Ландшафтный парк "Дворянское гнездо"',
               'Орел, Сквер 5-й Орловской стрелковой дивизии',
               'Орел, Литературный сквер'): ('pink','camera', photo_group),
              ('Орел, Бюст А.В. Горбатова',
               'Орел, Памятник И.С. Тургеневу в сквере у ж/д вокзала',
               'Орел, Памятник А.П. Ермолову'): ('orange', 'user', monument_group)}
