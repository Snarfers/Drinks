from flask import jsonify

from app import app
from app.models import Ingredient, Recipe, Instruction, Flavor


@app.route('/')
def index():
    return jsonify({'status': 'online'}), 200
