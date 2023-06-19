import vk_api
import random
from course1 import *
from vk_api.longpoll import VkLongPoll, VkEventType
from wiki import *
token = 'vk1.a.E-77HmhNLMuHqyup9xYpQjNsJLRC79jsbDjQGkvBZuTpVN1HemCQlXTcLIG6lqQlxu33OHDQjwBfK7sOEQou9jvedlB9nyqDFCOMQSW'\
       '7bq2vsZwi7FX8-y6KYvJpoBzfBu5iY8HrvCR1jO07Yw1YZB4U0LTEPQfQZAv-7DWSLcBe2MFnnvkKD4VniuYsRlGnjNZ8FlIM6DNNltKAwox16Q'
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        user_id = event.user_id
        random_id = random.randint(1, 10_000_000_000)
        if msg == 'привет':
            response = 'Привет :)'
        elif msg.startswith("-к"):
            response = f"{get_course(msg[3:].upper())} рублей за 1 " \
                       f"{xml.find('valute', {'id': msg[3:].upper()}).find('name').text}"
        elif msg.startswith("-в"):
            article = msg[2:]
            response = get_wiki_article(article)
        else:
            response = 'Я тебя не понимаю'
        vk.messages.send(user_id=user_id, random_id=random_id, message=response)

# планеты - дз
'''url = 'https://swapi.dev/api/'
response = requests.get(url).json()
planets_api = response.get('planets')
response = requests.get(planets_api).json()
Max = int(response['results'][0]["diameter"])
max_n = 0
for num in range(10):
    if Max <= int(response['results'][num]["diameter"]):
        Max = int(response['results'][num]["diameter"])
        max_n = num'''

# корабли - дз
'''url1 = 'https://swapi.dev/api/starships/'
url2 = 'https://swapi.dev/api/starships/?page=2'
url3 = 'https://swapi.dev/api/starships/?page=3'
url4 = 'https://swapi.dev/api/starships/?page=4'
urls = [url1, url2, url3]
response1 = requests.get(url1).json()
Max1 = int(response1['results'][0]["max_atmosphering_speed"])
ship = response1['results'][0]["name"]
for url in urls:
    response1 = requests.get(url).json()
    for num in range(10):
        if response1['results'][num]["max_atmosphering_speed"] == 'n/a' \
                or response1['results'][num]["max_atmosphering_speed"] == 'unknown'\
                or response1['results'][num]["max_atmosphering_speed"] == '1000km':
            pass
        elif Max1 <= int(response1['results'][num]["max_atmosphering_speed"]):
            Max1 = int(response1['results'][num]["max_atmosphering_speed"])
            ship = response1['results'][num]["name"]
response1 = requests.get(url4).json()
for n in range(6):
    if response1['results'][n]["max_atmosphering_speed"] == 'n/a' \
            or response1['results'][n]["max_atmosphering_speed"] == 'unknown' \
            or response1['results'][n]["max_atmosphering_speed"] == '1000km':
        pass
    elif Max1 <= int(response1['results'][n]["max_atmosphering_speed"]):
        Max1 = int(response1['results'][n]["max_atmosphering_speed"])
        ship = response1['results'][n]["name"]'''

'''while True:
    messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})
    if messages['count'] >= 1:
        print(messages)
        user_id = messages['items'][0]['last_message']['from_id']
        message_id = messages['items'][0]['last_message']['id']
        message_text = messages['items'][0]['last_message']['text']
        if message_text.lower() == 'привет':
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': 'Привет :)'})
        elif message_text.lower() == 'курс':
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id,
                                        'message': f'{get_course("R01235")} рублей за 1 доллар'})
        elif message_text.lower() == 'планеты':
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id,
                                        'message': f"Планета с макс. диаметром: {response['results'][max_n]['name']}"})
        elif message_text.lower() == 'корабли':
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id,
                                        'message': f"Корабль с макс.скоростью: {ship}"})
        else:
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': 'Не понимаю тебя'})
'''
