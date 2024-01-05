import json

class API_Keys:
    def __init__(self) -> None:
        self.config = json.load(open("config/api_keys.json"))
        
    @property
    def openAI_key(self):
        return self.config["openai"]
    
    @property
    def superhero_key(self):
        return self.config["superhero"]
  