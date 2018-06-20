import requests
import simplejson
import os
from yobit import get_btc
from time import sleep
from centrobank import get_eur

token = os.getenv('TELEGRAM_TOKEN')

URL = 'https://api.telegram.org/bot' + token + '/'

global last_update_id
last_update_id = 0


def get_updates():
    url = URL + 'getUpdates'
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()
    last_object = data['result'][-1]
    current_update_id = last_object['update_id']
    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id
        chat_id = last_object['message']['chat']['id']
        message_text = last_object['message']['text']
        message = {'chat_id': chat_id,
                   'text': message_text}
        return message
    return None


def send_message(chat_id, text='WASP'):
    url = URL + 'sendMessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def main():
    # d = get_updates()
    while True:
        answer = get_message()
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']
            # with open('updates.json', 'w') as file:
            # json.dump(d, file, indent=2, ensure_ascii=False)
            if text == '/btc':
                send_message(chat_id, get_btc())
            if text == '/love':
                send_message(chat_id, 'I Love Xenia')
            if text == '/etor':
                send_message(chat_id, 'Евро стоит ' + get_eur() + ' рублей')
        else:
            continue
        # with open('updates.json', 'w') as file:
        # json.dump(d, file, indent=2, ensure_ascii=False)
        sleep(3)


if __name__ == '__main__':
    main()