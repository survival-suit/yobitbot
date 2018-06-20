import requests

def get_eur():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url).json()
    price = response['Valute']['EUR']['Value']
    return str(price)