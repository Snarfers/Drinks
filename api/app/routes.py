from flask import jsonify

from app import app, db
from app.models import Ingredient, Recipe, Instruction, Flavor
from app.models import IngredientSchema, RecipeSchema

# Home Route
@app.route('/')
def index():
    return jsonify({'status': 'online'}), 200

#######################
## INGREDIENT ROUTES ##
#######################

# Create Ingredient
@app.route('/ingredient/new', methods=["POST"])
def ingredient_create():
    ingredient = Ingredient(**request.json)

    try:
        db.session.add(ingredient)
        db.session.commit()
    except:
        db.session.rollback()

    return jsonify({'status': 'success'}), 200


# List all ingredients
@app.route('/ingredient/all')
def ingredient_list():
    ingredients = Ingredient.query.all()
    result = IngredientSchema(many=True).dump(ingredients)
    return jsonify({"result": result.data}), 200


# Fetch single ingredient by name
@app.route('/ingredient/<string:name>')
def ingredient_find_name(name):
    ingredient = Ingredient.query.filter_by(name=name).first()
    result = IngredientSchema(many=False).dump(ingredient)
    return jsonify({"result": result.data}), 200


# Fetch single ingredient by id
@app.route('/ingredient/<int:id>')
def ingredient_find_id(id):
    ingredient = Ingredient.query.filter_by(id=id).first()
    result = IngredientSchema(many=False).dump(ingredient)
    return jsonify({"result": result.data}), 200

#######################
## RECIPE ROUTES ##
#######################

# Create Recipe
@app.route('/recipe/new', methods=["POST"])
def recipe_create():
    recipe = Recipe(**request.json)

    try:
        db.session.add(recipe)
        db.session.commit()
    except:
        db.session.rollback()

    return jsonify({'status': 'success'}), 200

# List all recipes
@app.route('/recipe/all')
def recipe_list():
    recipes = Recipe.query.all()
    result = RecipeSchema(many=True).dump(recipes)
    return jsonify({"result": result.data}), 200

# Fetch single recipe by name
@app.route('/recipe/find/<string:name>')
def recipe_find_name(name):
    recipe = Recipe.query.filter_by(name=name).first()
    result = RecipeSchema(many=False).dump(recipe)
    return jsonify({"result": result.data}), 200

# Fetch single recipe by id
@app.route('/recipe/find/<int:id>')
def recipe_find_id(id):
    recipe = Recipe.query.filter_by(id=id).first()
    result = RecipeSchema(many=False).dump(recipe)
    return jsonify({"result": result.data}), 200
