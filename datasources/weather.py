from datetime import datetime
import requests

URL = 'https://forecast.buienradar.nl/2.0/forecast/{}'
DATE_FORMAT = '%Y-%m-%dT%H:%M:%S'

BUIENRADAR_ICONS = {
    "a": "\uf00d",
    "b": "\uf002",
    "c": "\uf041",
    "d": "\uf001",
    "f": "\uf019",
    "g": "\uf01e",
    "h": "\uf019",
    "i": "\uf026",
    "j": "\uf002",
    "k": "\uf019",
    "l": "\uf019",
    "m": "\uf01c",
    "n": "\uf021",
    "o": "\uf002",
    "q": "\uf019",
    "r": "\uf002",
    "s": "\uf01e",
    "t": "\uf01b",
    "u": "\uf01b",
    "v": "\uf01b",
    "w": "\uf01b",
    "aa": "\uf02e",
    "bb": "\uf083",
    "cc": "\uf031",
    "dd": "\uf023",
    "ff": "\uf039",
    "gg": "\uf02c",
    "hh": "\uf032",
    "jj": "\uf031",
    "kk": "\uf039",
    "pp": "\uf041",
}

WIND_SCALE = {
    0: "\uf0b7",
    1: "\uf0b8",
    2: "\uf0b9",
    3: "\uf0ba",
    4: "\uf0bb",
    5: "\uf0bc",
    6: "\uf0bd",
    7: "\uf0be",
    8: "\uf0bf",
    9: "\uf0c0",
    10: "\uf0c1",
    11: "\uf0c2",
    12: "\uf0c3",
}


# TODO: wind icons do not work yet
WIND_DIRECTION = {
    "N": "\uf05c",
    "NW": "\uf0fb",
    "NO": "\uf05a",
    "Z": "\uf060",
    "ZW": "\uf05e",
    "ZO": "\uf05D",
    "O": "\uf059",
    "W": "\uf061",
}

def get_weather(code):
    r = requests.get(URL.format(code))
    future_data = r.json()
    return future_data['days']


class WeatherData():
    def __init__(self, code):
        r = requests.get(URL.format(code))
        self.days = r.json()['days']
        self.today = self.days[0]

    def windspeed(self):
        return WIND_SCALE.get(self.today['windspeed'])

    def winddirection(self):
        return WIND_DIRECTION.get(self.today['winddirection'])

    def sundata(self):
        now = datetime.now()
        sunrise = datetime.strptime(self.today['sunrise'], DATE_FORMAT)
        sunset = datetime.strptime(self.today['sunset'], DATE_FORMAT)
        if sunrise < now < sunset:
            sunicon = "\uf052"
            suntime = sunset
        else:
            suntime = sunrise
            sunicon = "\uf051"
        return sunicon, suntime

    def currenttemp(self):
        current_hour = self.today['hours'][0]
        iconcode = BUIENRADAR_ICONS.get(current_hour['iconcode'])
        current_temp = str(round(current_hour['temperature']))
        return iconcode, current_temp

    def minmax_today(self):
        mintemp = str(round(self.today['mintemperature']))
        maxtemp = str(round(self.today['maxtemperature']))
        return mintemp, maxtemp

    def forecast(self, days=4):
        data = []
        for index, day in enumerate(self.days):
            # Skip today
            if index == 0:
                continue

            if index == days+1:
                break

            data.append({
                'temp': '{} {}'.format(day['maxtemp'], day['mintemp']),
                'icon': BUIENRADAR_ICONS.get(day['iconcode']),
                'txt': datetime.strptime(day['datetime'], '%Y-%m-%dT%H:%M:%S').strftime('%a')
            })
        return data
