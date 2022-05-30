import json
import flask
from flask import jsonify, request
import mysql.connector as mysql

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# setup connect and execute provided query
def connect(query):
    db = mysql.connect(
        host = "192.168.3.70",
        user = "root",
        passwd = "challenge",
        database = "api_agg"
    )
    cursor = db.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows

col_names = ['idMeal', 'strMeal', 'strDrinkAlternate', 'strCategory', 
    'strArea', 'strInstructions', 'strMealThumb', 'strTags', 'strYoutube', 
    'strIngredient1', 'strIngredient2', 'strIngredient3', 'strIngredient4', 
    'strIngredient5', 'strIngredient6', 'strIngredient7', 'strIngredient8', 
    'strIngredient9', 'strIngredient10', 'strIngredient11', 'strIngredient12', 
    'strIngredient13', 'strIngredient14', 'strIngredient15', 'strIngredient16', 
    'strIngredient17', 'strIngredient18', 'strIngredient19', 'strIngredient20', 
    'strMeasure1', 'strMeasure2', 'strMeasure3', 'strMeasure4', 'strMeasure5', 
    'strMeasure6', 'strMeasure7', 'strMeasure8', 'strMeasure9', 'strMeasure10', 
    'strMeasure11', 'strMeasure12', 'strMeasure13', 'strMeasure14', 
    'strMeasure15', 'strMeasure16', 'strMeasure17', 'strMeasure18', 
    'strMeasure19', 'strMeasure20', 'strSource', 'strImageSource', 
    'strCreativeCommonsConfirmed', 'dateModified']

# search meal by name
@app.route('/search_name/<string:name>', methods=['GET'])
def search_meal_name(name):
    query = f"SELECT * FROM meals WHERE strMeal='{name}'"
    rows = connect(query=query)
    i = 0
    meals = {}
    for row in rows:
        combined_result = dict(zip(col_names, row))
        meals[i] = combined_result
        i += 1
    return jsonify(meals)

# search meal by main ingredient
@app.route('/search_main_ingredient/<string:name>', methods=['GET'])
def search_main_ingredient(name):
    query = f"SELECT * FROM meals WHERE strCategory='{name}'"
    rows = connect(query=query)
    i = 0
    meals = {}
    for row in rows:
        combined_result = dict(zip(col_names, row))
        meals[i] = combined_result
        i += 1
    return jsonify(meals)

# get cooking instructions based on idMeal [the id number]
@app.route('/search_instructions/<string:id>', methods=['GET'])
def search_instructions(id):
    query = f"SELECT * FROM instructions where idMeal='{id}'"
    rows = connect(query=query)
    i = 0
    meals = {}
    for row in rows:
        combined_result = dict(zip(col_names, row))
        meals[i] = combined_result
        i += 1
    return jsonify(meals)

# search for all meals with 2 ingredients 
# can search with AND or OR
@app.route('/filter_by_ingredients', methods=['GET'])
def filter_by_ingredients():
    args = request.args
    ingredient1 = args.get('ingredient1')
    ingredient2 = args.get('ingredient2')
    selector = args.get('and_or_or')
    query = f"""select * from meals where '{ingredient1}' in (
        strIngredient1, strIngredient2, strIngredient3,
        strIngredient4, strIngredient5, strIngredient6, strIngredient7,
        strIngredient8, strIngredient9, strIngredient10, strIngredient11,
        strIngredient12, strIngredient13, strIngredient14, 
        strIngredient15, strIngredient16, strIngredient17,
        strIngredient18, strIngredient19,strIngredient20)
        {selector} '{ingredient2}' in (
        strIngredient1, strIngredient2, strIngredient3,
        strIngredient4, strIngredient5, strIngredient6, strIngredient7,
        strIngredient8, strIngredient9, strIngredient10, strIngredient11,
        strIngredient12, strIngredient13, strIngredient14, 
        strIngredient15, strIngredient16, strIngredient17,
        strIngredient18, strIngredient19,strIngredient20)"""
    rows = connect(query=query)
    i = 0
    meals = {}
    for row in rows:
        combined_result = dict(zip(col_names, row))
        meals[i] = combined_result
        i += 1
    return jsonify(meals)


app.run(port=4444)