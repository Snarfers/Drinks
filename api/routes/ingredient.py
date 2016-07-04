import json

from flask import request, jsonify, abort

from app import app, db, row_to_dict
from app import COMMON

#Importing models
from models.ingredient import Ingredient


@app.route(COMMON['API_ROUTE'] + '/ingredient/all', methods=['GET'])
def ingredient_all():
  try:
    ingredients = Ingredient.query.all()
    response = [row_to_dict(ingredient) for ingredient in ingredients]
  except:
    abort(500)

  return jsonify(response)


@app.route(COMMON['API_ROUTE'] + '/ingredient/<int:index>')
def ingredient_index(index):
  ingredient = Ingredient.query.filter_by(id=index).first()

  if(ingredient == None):
    abort(404)

  response = row_to_dict(ingredient)

  return jsonify(response)


@app.route(COMMON['API_ROUTE'] + '/ingredient/create', methods=['POST'])
def ingredient_create():
  data = request.get_json()

  try:
    db.session.add(Ingredient(name=data['name']))
    db.session.commit()
  except:
    abort(500)

  return jsonify(COMMON['SUCCESS'])
