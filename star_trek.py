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
# Trying to a new way to get data from the API
# at the moment I need a way to get the next page


# def get_data(entity, page_number):
#     """Gets data from the Star Trek API"""
    
#     url = f"{BASE_URL}/{entity}/search"
#     params = {"pageNumber": page_number}
    
#     try:
#         res = requests.get(url, params=params)
#         res.raise_for_status()
#         data = res.json()
#         return data
#     except requests.exceptions.HTTPError as err:
#         print(err)
#         return None

# x = get_data("character", 3)

# BASE_URL = "https://stapi.co/api/v1/rest"

# def get_data(entity, page_number):
#     """Gets data from the Star Trek API"""
    
#     params = {"pageNumber": page_number}
#     res = requests.get(f"{BASE_URL}/{entity}/search?page?pageNumber={page_number}")
    
#     try:
#         res.raise_for_status()
#         data = res.json()
#         while data["page"]["lastPage"] is not True:
#             page_number += 1
#             print("next page found, downloading", data["page"]["pageNumber"])
#             res = requests.get(f"{BASE_URL}/{entity}/search?page?pageNumber={page_number}")
            
#             return data
        
        
#     except requests.exceptions.HTTPError as err:
#         print(err)
#         return None
    
# x = get_data("character", 0)
# print(x["page"]['lastPage'])

# # ?how to get the next page
# # ?how do you turn json data into a python object
# def get_all_characters():
#     page_number = 1
#     while True:
#         params = {"pageNumber": page_number}
#         response = requests.get("https://stapi.co/api/v1/rest/character", params=params)
#         data = response.json()
#         characters = data["characters"]
#         # process the characters data
#         for character in characters:
#             print(character)
#         if data["pageNumber"] == data["pageCount"]:
#             break
#         page_number += 1
        
# y = get_all_characters()
# y["page"]["pageNumber" == "pageCount"]

BASE_URL = "https://stapi.co/api/v1/rest"
def get_data(entity, page_number):
    """Gets data from the Star Trek API"""
    
    url = f"{BASE_URL}/{entity}/search"
    params = {"pageNumber": page_number}
    
    try:
        res = requests.get(url, params=params)
        res.raise_for_status()
        data = res.json()
        return data
    except requests.exceptions.HTTPError as err:
        print(err)
        return None
    
def get_total_pages(entity):
    """Gets the total number of pages for a given entity"""
    
    res = get_data(entity, 1)
    data = res["page"]
    total = data["totalPages"]
    return total

  
 #get all the data for a given entity    


x = get_data("character", 3)
y = get_total_pages("character")

# for each page in the total pages make a call to the api and save them 
# for page in range(1, y + 1):
#     print(page)
#     data = get_data("character", page)
#     print(data[2])

def save_entity(entity):
    """Saves the data to the json file"""
    
    y = get_total_pages(entity)
    pages = []
    # does can a range start at 0
    for page in range(0, y + 1):
        data = get_data(entity, page)
        pages.append(page)
        with open(f'data/{entity}.json', 'a') as file:
            file.seek(0)
            json.dump(data, file, indent=4)
        

save_entity("character")
        

    



        
        
