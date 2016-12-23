from flask import request, jsonify, abort

from .. import app, db, COMMON, row_to_dict

# Importing models
from ..models.recipe import Recipe


@app.route('/api/recipe/all', methods=['GET'])
def recipe_all():
    recipes = Recipe.query.all()
    response = []

    return jsonify(response)


@app.route('/api/recipe/<int:index>')
def recipe_index(index):
    recipe = Recipe.query.filter_by(id=index).first()

    if(recipe == None):
        abort(404)

    response = row_to_dict(recipe)

    return jsonify(response)


# TODO: Complete the route for creating a recipe
@app.route('/api/recipe/create', methods=['POST'])
def recipe_create():
    recipe = request.get_json()

    try:
        recipe = Recipe(**recipe)
        db.session.add(recipe)
        db.session.commit()
    except:
        db.session.rollback()
        abort(500)


    return jsonify(COMMON['SUCCESS'])
