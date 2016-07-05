from flask import Flask, jsonify, abort

from app import app

import json

from models.ingredient import Ingredient
from models.portion import Portion

from routes.ingredient import ingredient_all, ingredient_index, ingredient_create


db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
