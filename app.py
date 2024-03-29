from flask import Flask, request, jsonify, render_template

from api import *
from config.config import API_Keys

api_keys = API_Keys()

chatbot_api = chatbot_api.openAIChatbot(api_keys.openAI_key)
superhero_api = superhero_api.Superhero(api_keys.superhero_key)
popcat_api = popcat_api.popCat()
anime_api = anime_api.Anime()

app = Flask("Wizardi API")


app.endpoint('chat_get')
app.endpoint('superhero')
app.endpoint('element')
app.endpoint('pickup')
app.endpoint('meme')
app.endpoint('joke')
app.endpoint('fact')
app.endpoint('lulcat')
app.endpoint('weather')
app.endpoint('quote')
app.endpoint('shower_thoughts')
app.endpoint('anime')
app.endpoint('anime_character')
app.endpoint('anime_news')
app.endpoint('anime_waifu')



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['GET'])
def chat_get():
    user_input = request.args.get('user_input')
    chat_response = chatbot_api.chat_prompt(user_input)
    return jsonify({"response": chat_response})

@app.route('/superhero', methods=['GET'])
def superhero():
    name = request.args.get('name')
    return superhero_api.get_data(name)
    
@app.route('/element', methods=['GET'])
def element():
    element = request.args.get('element')
    return popcat_api.element_data(element)

@app.route('/pickup-lines', methods=['GET'])
def pickup():
    return popcat_api.pickup_lines()

@app.route('/meme', methods=['GET'])
def meme():
    return popcat_api.meme()

@app.route('/joke', methods=['GET'])
def joke():
    return popcat_api.joke()

@app.route('/fact', methods=['GET'])
def fact():
    return popcat_api.fact()

@app.route('/lulcat', methods=['GET'])
def lulcat():
    text = request.args.get('text')
    return popcat_api.lulcat(text)

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')
    return popcat_api.weather(city)

@app.route('/quote', methods=['GET'])
def quote():
    return popcat_api.quote()

@app.route('/shower-thoughts', methods=['GET'])
def shower_thoughts():
    return popcat_api.shower_thoughts()

@app.route('/anime/info', methods=['GET'])
def anime():
    name = request.args.get('name')
    return jsonify(anime_api.animeData(name))

@app.route('/anime/character', methods=['GET'])
def anime_character():
    name = request.args.get('name')
    return jsonify(anime_api.animeCharacter(name))

@app.route('/anime/news', methods=['GET'])
def anime_news():
    return jsonify(anime_api.animeNews())

@app.route('/anime/waifu', methods=['GET'])
def anime_waifu():
    kind = request.args.get('kind')
    return anime_api.animeWaifu(kind)
    

app.run(debug=True)
