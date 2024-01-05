import requests
import json


class Superhero:
    def __init__(self, api_key):
        self.search_url = f"https://superheroapi.com/api/{api_key}/search/"
    
    def get_data(self, name):
        req = requests.get(f"{self.search_url}{name}")
        data = json.loads(req.text)
        return data