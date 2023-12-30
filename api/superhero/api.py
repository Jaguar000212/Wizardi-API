import requests
import json


def get_data(name):
    req = requests.get(
        f"https://superheroapi.com/api/2527790687387610/search/{name}"
    )
    data = json.loads(req.text)
    return data