import requests

URL = 'https://forecast.buienradar.nl/2.0/forecast/{}'


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
    "ZO": "\uf05d",
    "O": "\uf059",
    "W": "\uf061",
}

def get_weather(code):
    r = requests.get(URL.format(code))
    future_data = r.json()
    return future_data['days']
