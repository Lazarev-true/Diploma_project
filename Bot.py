import requests
import time

version = 5.131
token = 'b15d7df9b15d7df9b15d7df91fb2480f70bb15db15d7df9d5b604d5abb3dfa88dd59888'  
domains = {'-97221815': 0, '-210044251': 0, '-48572216': 0, '-60024751': 0}
tg_token = '6143872426:AAFR8kPPREzy829yijw6DKwZvSXwDQ4VyZw'
tg_channel_id = '@events_orel'  

while True:
    vk_api_url = 'https://api.vk.com/method/wall.get'
    for domain, latest_post in domains.items():
        offset = 0
        while True:
            vk_params = {
                'owner_id': domain,
                'count': 1,
                'offset': offset,
                'access_token': token,
                'v': version,
            }
            response = requests.get(vk_api_url, params=vk_params)
            data = response.json()
            if 'response' in data:
                posts = data['response']['items']
                if len(posts) == 0:
                    print(f'Нет новых незакрепленных постов в группе {domain}')
                    break
                post = posts[0]
                if 'is_pinned' in post and post['is_pinned'] == 1:
                    offset += 1
                    continue
                if post['id'] == latest_post:
                    print(f'Ждём ещё 10 минут для группы {domain}')
                    break
                if 'attachments' in post and len(post['attachments']) > 0 and post['attachments'][0]['type'] == 'photo':
                    tg_api_url = f'https://api.telegram.org/bot{tg_token}/sendMessage'
                    tg_params = {
                        'chat_id': tg_channel_id,
                        'text': f"{post['text']}\n\n{post['attachments'][0]['photo']['sizes'][-1]['url']}"
                    }
                    response = requests.post(tg_api_url, data=tg_params)
                    result = response.json()
                    if result['ok']:
                        print(f'Сообщение успешно отправлено в Telegram из группы {domain}')
                    else:
                        print(f'Ошибка при отправке сообщения в Telegram из группы {domain}')
                    domains[domain] = post['id']
                    break
                offset += 1
            else:
                print(f"Ошибка при получении сообщений из ВК для группы {domain}: {data['error']['error_msg']}")

    time.sleep(300)