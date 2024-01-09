import requests
from bs4 import BeautifulSoup

def get_image_url(keyword):
    # Отправляем запрос к Google Images
    url = f"https://www.google.com/search?q={keyword}&tbm=isch"
    response = requests.get(url)

    # Создаем объект BeautifulSoup для парсинга страницы
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим все теги <img> на странице
    images = soup.find_all('img')

    images_url_lst = []

    # Ссылки на изображения
    images_url_lst = [image['src'] for image in images]

    return images_url_lst[1]