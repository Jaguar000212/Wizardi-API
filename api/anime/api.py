import animec
import inspect

import requests

class Anime:
    
    @staticmethod
    def animeData(name):
        
        anime = animec.Anime(name)
        
        try:
            data = {
                "name" : anime.name,
                "info_page" : anime.url,
                "title_en" : anime.title_english,
                "title_jp" : anime.title_jp,
                "alt_titles" : anime.alt_titles,
                "poster" : anime.poster,
                "description" : anime.description,
                "genres" : anime.genres,
                "type" : anime.type,
                "nsfw" : anime.is_nsfw(),
                "episodes" : anime.episodes,
                "aired" : anime.aired,
                "braodcast" : anime.broadcast,
                "premiered" : anime.premiered,
                "rating" : anime.rating,
                "ranked" : anime.ranked,
                "popularity" : anime.popularity,
                "favorites" : anime.favorites,
                "status" : anime.status,
                "producers" : anime.producers,
                "teaser" : anime.teaser,
                "recommendations" : anime.recommend(),
            }
        
            return data
        except AttributeError:
            return {"error" : "Anime not found."}
    
    @staticmethod
    def animeCharacter(name):
        character = animec.Charsearch(name)
        
        try:
            data = {
                "name" : character.title,
                "info_page" : character.url,
                "image" : character.image_url,
                "references" : character.references,
            }
            
            return data
        except AttributeError:
            return {"error" : "Character not found."}
    
    @staticmethod
    def animeNews():
        
        news = animec.Aninews(8)
        data = {}
        
        try:
            for i in range(8):
                data[f"news_{i}"] = {
                        "title" : news.titles[i],
                        "link" : news.links[i],
                        "description" : news.description[i],
                }
            return data
        except:
            return {"error" : "Something went wrong."}
    
    @staticmethod
    def animeWaifu(kind):
        waifu = animec.Waifu()
        available = ['awoo', 'bite', 'blush', 'bonk', 'bully', 'cringe', 'cry', 'cuddle', 'dance', 'glomp', 'handhold', 'happy', 'highfive', 'hug', 'kick', 'kill', 
                     'kiss', 'lick', 'megumin', 'neko', 'nom', 'pat', 'poke', 'random', 'random_gif', 'shinobu', 'slap', 'smile', 'smug', 'waifu', 'wink', 'yeet']
                    
        if kind not in available:
            return {"error" : "Invalid type."}
        

        response = requests.get(f"https://api.waifu.pics/sfw/{kind}")
        return response.json()
