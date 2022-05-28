import requests
import json

meal = requests.request('GET', f'http://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata').json
print(json.dumps(meal))

##


import requests
import json

def get_ingredients(data):
    ingredients = {}
    for item in data['meals']:
        id = item['idMeal']
        details = requests.request('GET', 'http://www.themealdb.com/api/json/v1/1/lookup.php?i=53016').text()#{id}').text
        detail_json = json.loads(details)
        ingredients[id] = detail_json['meals']
    return ingredients

meals = requests.request('GET', f'http://www.themealdb.com/api/json/v1/1/filter.php?i=chicken_breast').text
data = json.loads(meals)
details = get_ingredients(data=data)


"""
client = pymongo.MongoClient("mongodb://192.168.3.70:27017")
db = client['append']
collection = db['appenddata']
file = details
collection.insert_many(file)
# or instert_one(file)
"""