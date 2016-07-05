from flask import Flask, jsonify, abort

import json


#Ingredients Routes
@app.route('/ingredients/all', methods=['GET'])
def ingredientsAll():

    return response

@app.route('/ingredients/<int:ingredient_id>', methods=['GET'])
def ingredients(ingredient_id):

    return response

if __name__ == '__main__':
    app.run(debug=True)
