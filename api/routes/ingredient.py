from flask import request, jsonify, abort

from api import app, db, COMMON, row_to_dict

# Importing models
from api.models.ingredient import Ingredient
from api.models.portion import Portion


@app.route('/api/ingredient/all', methods=['GET'])
def ingredient_all():
    ingredients = Ingredient.query.all()
    response = [row_to_dict(ingredient) for ingredient in ingredients]

    return jsonify(response)


@app.route('/api/ingredient/<int:index>')
def ingredient_index(index):
    ingredient = Ingredient.query.filter_by(id=index).first()

    if(ingredient == None):
        abort(404)

    response = row_to_dict(ingredient)

    return jsonify(response)


@app.route('/api/ingredient/<string:category>')
def ingredient_category(category):
    ingredients = Ingredient.query.filter_by(category=category).all()

    if len(ingredients) == 0:
        abort(404)

    response = [row_to_dict(ingredient) for ingredient in ingredients]

    return jsonify(response)


@app.route('/api/ingredient/create', methods=['POST'])
def ingredient_create():
    ingredient = request.get_json()

    try:
        db.session.add(Ingredient(**ingredient))
        db.session.commit()
    except:
        db.rollback()

    return jsonify(COMMON['SUCCESS'])
