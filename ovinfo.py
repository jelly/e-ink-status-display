import requests

from config import OVID

URL = 'http://api.9292.nl/0.1/locations/{}/departure-times?lang=nl-NL'


def get_departures(limit=4):
    data = []

    r = requests.get(URL.format(OVID))
    tabs = r.json()['tabs']
    for vehicle in tabs:
        for index, departure in enumerate(vehicle['departures']):
            if index == limit:
                break
            data.append("{} - {} {} {}".format(
                departure['time'],
                vehicle['name'],
                departure['service'],
                departure['destinationName'],
            ))

    return data
