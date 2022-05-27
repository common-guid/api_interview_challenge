import flask
from flask import request, jsonify
import requests
import json
import pandas as pd

def get_ingredients(data):
    ingredients = {}
    for item in data['meals']:
        id = item['idMeal']
        details = requests.request('GET', f'http://www.themealdb.com/api/json/v1/1/lookup.php?i={id}').text
        detail_json = json.loads(details)
        ingredients[id] = detail_json['meals']
    return ingredients

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/search_name/<string:name>', methods=['GET'])
def request_meal(name):
    meal = requests.request('GET', f'http://www.themealdb.com/api/json/v1/1/search.php?s={name}').text
    j = json.loads(meal)
    tbl = pd.json_normalize(j)
    return 

@app.route('/main_ingredient/<string:name>', methods=['GET'])
def request_by_ingredient(name):
    meals = requests.request('GET', f'http://www.themealdb.com/api/json/v1/1/filter.php?i={name}').text
    data = json.loads(meals)
    return get_ingredients(data=data)

@app.route('/category/<string:name>', methods=['GET'])
def request_by_cat(name):
    meals = requests.request('GET', f'http://www.themealdb.com/api/json/v1/1/filter.php?c={name}').text
    data = json.loads(meals)
    return get_ingredients(data=data)

@app.route('/region/<string:name>', methods=['GET'])
def request_by_region(name):
    meals = requests.request('GET', f'http://www.themealdb.com/api/json/v1/1/filter.php?a={name}').text
    data = json.loads(meals)
    return get_ingredients(data=data)

app.run(port=5555)