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
        
trek = StarTrekAPI()
chars = trek.get_characters()

char = [char for char in chars]
# print(char)
# turn the json data into a list of dictionaries
json_data = json.dumps(char)
print(len(json_data))












