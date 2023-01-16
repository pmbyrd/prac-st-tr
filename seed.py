import requests

url = "http://stapi.co/api/v1/rest/"

api_list = [
        'company', 
    'comicStrip', 
    'organization', 
    'soundtrack', 
    'character', 
    'common', 
    'literature', 
    'magazine', 
    'videoRelease', 
    'animal', 
    'comicCollection', 
    'staff', 
    'common', 
    'title',
    'astronomicalObject', 
    'element', 
    'common', 
    'tradingCard', 
    'comics', 
    'tradingCardDeck', 
    'magazineSeries', 
    'videoGame', 
    'technology', 
    'comicSeries', 
    'movie', 
    'performer', 
    'weapon', 
    'episode', 
    'season', 
    'bookSeries', 
    'conflict', 
    'location', 
    'spacecraftClass', 
    'material', 
    'species', 
    'occupation', 
    'bookCollection', 
    'medicalCondition', 
    'food', 
    'tradingCardSet', 
    'oauth', 
    'book', 
    'spacecraft', 
    'series'
]

res = requests.get("url/'actor'")

# make a 