import requests
import json

meal = requests.request('GET', f'http://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata').json
print(json.dumps(meal))

##

import pymongo

client = pymongo.MongoClient("mongodb://192.168.3.70:27017")
db = client['testdf']
collection = db['dftest']
file = 
collection.insert_many(file)
# or instert_one(file)
