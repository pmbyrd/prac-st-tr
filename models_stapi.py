#
# * This file is used to make the calls to the STAPI API to get the data for the database

import requests
import stapi
import json
from stapi import search_criteria, common_search_criteria

# *for practice all methods about the api will be in this one class

class StarTrekAPI:
    """Uses stapi methods to get data from the Star Trek API"""
    
    def __init__(self):
        self.url = "https://stapi.co/api"
        
    def get_characters(self):
        """Gets all the characters from the Star Trek API"""
            
        characters = []
        
        url = f"{self.url}/v1/rest/character/search?title=Star Trek"
        
        try:
            res = requests.get(url)
            data = res.json()
            res.raise_for_status()
            characters.extend(data["characters"])
            return characters
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        
   
    def get_character_by_id(self, character_id):
        url = f"{self.base_url}/v1/rest/character/{character_id}"
        params = {"apiKey": self.api_key}
        response = requests.get(url, params=params)
        return response.json()

            
        
        
        
            
        
trek = StarTrekAPI()
chars = trek.get_characters()

char = [char for char in chars]
# print(char)
# turn the json data into a list of dictionaries
data = json.loads(json.dumps(char))
c = data[0]["uid"]

# print(len(json_data))
print(char[0:5])













