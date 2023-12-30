import requests
import json

def element_data(name):
    req = requests.get(
        f"https://api.popcat.xyz/periodic-table?element={name}"
    )
    data = json.loads(req.text)
    return data

def pickup_lines():
    req = requests.get(
        f"https://api.popcat.xyz/pickuplines"
    )
    data = json.loads(req.text)
    return data

def meme():
    req = requests.get(
        f"https://api.popcat.xyz/meme"
    )
    data = json.loads(req.text)
    return data

def joke():
    req = requests.get(
        f"https://api.popcat.xyz/joke"
    )
    data = json.loads(req.text)
    return data

def fact():
    req = requests.get(
        f"https://api.popcat.xyz/fact"
    )
    data = json.loads(req.text)
    return data

def lulcat(text):
    req = requests.get(
        f"https://api.popcat.xyz/lulcat?text={text}"
    )
    data = json.loads(req.text)
    return data

def weather(city):
    req = requests.get(
        f"https://api.popcat.xyz/weather?q={city}"
    )
    data = json.loads(req.text)
    return data

def quote():
    req = requests.get(
        f"https://api.popcat.xyz/quote"
    )
    data = json.loads(req.text)
    return data

def shower_thoughts():
    req = requests.get(
        f"https://api.popcat.xyz/showerthoughts"
    )
    data = json.loads(req.text)
    return data