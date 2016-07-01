from flask import Flask, jsonify, abort

import json

app = Flask(__name__)

#Data Imports
with open("data/ingredients.json") as ingredients:
    ingredients_data = json.load(ingredients)
    print(ingredients)

#End Data Imports


#Ingredients Routes
@app.route('/ingredients/all', methods=['GET'])
def ingredientsAll():
    response = jsonify(ingredients_data)
    response.status_code = 200
    return response

@app.route('/ingredients/<int:ingredient_id>', methods=['GET'])
def ingredients(ingredient_id):
    ingredient = [ingredient for ingredient in ingredients_data if ingredient['id'] == ingredient_id]

    if len(ingredient) == 0:
        abort(400)

    response = jsonify(ingredient[0])
    response.status_code = 200

    return response

if __name__ == '__main__':
    app.run(debug=True)
