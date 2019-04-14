import requests

URL = 'https://forecast.buienradar.nl/2.0/forecast/{}'

def get_weather(code):
    r = requests.get(URL.format(code))
    future_data = r.json()
    return future_data['days']
