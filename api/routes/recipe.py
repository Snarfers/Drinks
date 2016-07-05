import json

from flask import request, jsonify, abort

from app import app, db, row_to_dict
from app import COMMON

#Importing models
from models.recipe import Recipe


@app.route(COMMON['API_ROUTE'] + '/recipe/all', methods=['GET'])
def recipe_all():
    recipes = Recipe.query.all()
    response = []

    for recipe in recipes:
        recipe_data = {}
        recipe_data['name'] = recipe.name
        recipe_data['ingredients'] = []
        for ingredient in recipe.ingredients:
            ingredient_data = {}
            ingredient_data['name'] = ingredient.ingredient.name
            ingredient_data['portion'] = {"name": ingredient.portion.name, "abbriviation": ingredient.portion.abbrivation}
            ingredient_data['quantity'] = ingredient.quantity
            recipe_data['ingredients'].append(ingredient_data)
        response.append(recipe_data)

    return jsonify(response)


@app.route(COMMON['API_ROUTE'] + '/recipe/<int:index>')
def recipe_index(index):
    recipe = recipe.query.filter_by(id=index).first()

    if(recipe == None):
        abort(404)

    response = row_to_dict(recipe)

    return jsonify(response)


@app.route(COMMON['API_ROUTE'] + '/recipe/create', methods=['POST'])
def recipe_create():
    data = request.get_json()

    try:
        db.session.add()
        db.session.commit()
    except:
        abort(500)

    return jsonify(COMMON['SUCCESS'])
