import flask
import requests
import json
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    'mysql+mysqlconnector://root:challenge@192.168.3.70/api_agg')

## takes the idMeal #s returned from queries and searches each by idMeal
## this returns detailed info about the dishes
## detailed info is then parsed and split into 2 tables [instruction field was too long on occasion]
## both tables are inserted to MySQL by sql alchemy and pandas
## finally json data is returned for display on webpage
def get_ingredients(data):
    ingredients = {}
    combine_df, instructions_df = pd.DataFrame(), pd.DataFrame()
    for item in data['meals']:
        id = item['idMeal']
        details = requests.request('GET', f'http://www.themealdb.com/api/json/v1/1/lookup.php?i={id}').text
        detail_json = json.loads(details)
        # for display
        ingredients[id] = detail_json['meals']
        # for upload
        tbl = pd.json_normalize(detail_json['meals'])
        instructions = tbl[['idMeal','strInstructions']]
        tbl = tbl.drop('strInstructions', axis=1)
        # append details to combine and id+instructions to instructions df
        instructions_df = instructions_df.append(instructions, ignore_index=True)
        combine_df = combine_df.append(tbl, ignore_index=True)
    combine_df.to_sql(name='meals', con=engine, if_exists='append', index=False)
    instructions_df.to_sql(name='instructions', con=engine, if_exists='append', index=False)
    return ingredients

app = flask.Flask(__name__)
app.config["DEBUG"] = False

# search the mealdb by dish name
@app.route('/search_name/<string:name>', methods=['GET'])
def request_meal(name):
    meal = requests.request('GET', f'http://www.themealdb.com/api/json/v1/1/search.php?s={name}').text
    data = json.loads(meals)
    return get_ingredients(data=data)

# search the mealdb by main ingredient
@app.route('/main_ingredient/<string:name>', methods=['GET'])
def request_by_ingredient(name):
    meals = requests.request('GET', f'http://www.themealdb.com/api/json/v1/1/filter.php?i={name}').text
    data = json.loads(meals)
    return get_ingredients(data=data)

# search the mealdb by category
@app.route('/category/<string:name>', methods=['GET'])
def request_by_cat(name):
    meals = requests.request('GET', f'http://www.themealdb.com/api/json/v1/1/filter.php?c={name}').text
    data = json.loads(meals)
    return get_ingredients(data=data)

#search the mealdb by region
@app.route('/region/<string:name>', methods=['GET'])
def request_by_region(name):
    meals = requests.request('GET', f'http://www.themealdb.com/api/json/v1/1/filter.php?a={name}').text
    data = json.loads(meals)
    return get_ingredients(data=data)

app.run(port=5555)