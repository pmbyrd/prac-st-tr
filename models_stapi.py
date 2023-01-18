#


# * This file is used to make the calls to the STAPI API to get the data for the database

# !we are looking at a list of all endpoints and selecting the ones we want to use
# *
# *['organization', 
# *'character', 
# *'common',
# *'title',
# *'astronomicalObject', 
# *'element',
# *'tradingCard',
# *'technology',
# *'movie',
# *'performer',
# *'episode',
# *'season',
# *'conflict',
# *'location',
# *'spacecraftClass', 
# *'species',
# *'occupation',
# *'food', 
# * 'spacecraft', 
# *'series']

import requests
from pathlib import Path
import json
from stapi import search_criteria, common_search_criteria

# *for practice all methods about the api will be in this one class

class StarTrekAPI:
    """Uses stapi methods to get data from the Star Trek API"""
    
    def __init__(self):
        self.url = "https://stapi.co/api"
        
    def get_characters(self, page_number=1):
        """Gets all the characters from the Star Trek API"""
            
        characters = []
        params = {"pageNumber" = self.page_}
        
        url = f"{self.url}/v1/rest/character/search?"
        
        
        try: 
            res = requests.get(url, params=params)
            data = res.json()
            res.raise_for_status()
            
            # This condition is to check if there is a next page
            # if there is a next page, then we need to make another call to get the next page
            while data['page']['lastPage'] is not True:
                print("next page found, downloading", data['page']['pageNumber'])
                res = requests.get(url)
                characters.extend(data["characters"])
                return characters
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)    
        
        
   
    def get_character(self, uid):
        """Gets a single character from the Star Trek API"""
        url = f"{self.url}/v1/rest/character?uid={uid}"
        
        try:
            res = requests.get(url)
            data = res.json()
            res.raise_for_status()
            return data
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

            
    def get_ships(self):
        """Gets all the ships from the Star Trek API"""
        
        ships = []
        url = f"{self.url}/v1/rest/spacecraft/search?title=Star Trek"
        
        try:
            res = requests.get(url)
            data = res.json()
            res.raise_for_status()
            ships.extend(data["spacecrafts"])
            return ships            
            
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        
    def get_trading_cards(self):
        """Testing if there is a trading cards endpoint"""
        
        trading_cards = []
        url = f"{self.url}/v1/rest/tradingCard/search?title=Star Trek"
        
        try:
            res = requests.get(url)
            data = res.json()
            res.raise_for_status()
            trading_cards.extend(data["tradingCards"])
            return trading_cards
        
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        
def save_all_character_json():
    """Saves all the character data to a json file"""
    
    # make a call using stapi to get all the characters
    
    trek = StarTrekAPI()
    characters = trek.get_characters()
    # write this straight to the json file
    # with open("json/characters.json", "w") as f:
    #     json.dump(characters, f, indent=4)
    Path('data/characters.json').write_text(json.dumps(characters, indent=4))    
    
save_all_character_json()



            
    
            
            
            
        
        
        
        
        
            
        
trek = StarTrekAPI()
chars = trek.get_characters()

char = [char for char in chars]
# print(char)
# turn the json data into a list of dictionaries
data = json.loads(json.dumps(char))
c = data[0]["uid"]

# print(len(json_data))
print(char[0:5])













