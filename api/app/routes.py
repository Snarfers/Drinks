from flask import jsonify

from app import app
from app.models import Ingredient, Recipe, Instruction, Flavor

# Home Route
@app.route('/')
def index():
    return jsonify({'status': 'online'}), 200

#######################
## INGREDIENT ROUTES ##
#######################

# Create Ingredient
@app.route('/ingredient/new')
def ingredient_create():
    return jsonify({'status': 'route not currently implemented'}), 501


# List all ingredients
@app.route('/ingredient/all')
def ingredient_list():
    return jsonify({'status': 'route not currently implemented'}), 501


# Fetch single ingredient by name
@app.route('/ingredient/<string:name>')
def ingredient_find_name(name):
    return jsonify({'status': 'route not currently implemented'}), 501


# Fetch single ingredient by id
@app.route('/ingredient/<int:id>')
def ingredient_find_id(id):
    return jsonify({'status': 'route not currently implemented'}), 501


#######################
## RECIPE ROUTES ##
#######################

# Create Recipe
@app.route('/recipe/new')
def recipe_create():
    return jsonify({'status': 'route not currently implemented'}), 501


# List all recipes
@app.route('/recipe/all')
def recipe_list():
    return jsonify({'status': 'route not currently implemented'}), 501


# Fetch single recipe by name
@app.route('/recipe/find/<string:name>')
def recipe_find_name(name):
    return jsonify({'status': 'route not currently implemented'}), 501


# Fetch single recipe by id
@app.route('/recipe/find/<int:id>')
def recipe_find_id(id):
    return jsonify({'status': 'route not currently implemented'}), 501
