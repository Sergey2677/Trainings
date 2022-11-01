import requests
from time import sleep
from jinja2 import Template


url = ""


def get_updates_json(request, method='getUpdates'):
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()


def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

def main():
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
            text = '{{ name }}'
            template = Template(text)
            name = '''Привет! \
Я искуственный интелект VoiceAssistantForDailyTasks,\
и я помогу тебе работать с твоими ежедневными задачами!'''
            send_mess(get_chat_id(last_update(get_updates_json(url))), template.render(name=name))
            update_id += 1
            sleep(1)

if __name__ == '__main__':
    main()
