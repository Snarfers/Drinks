from app import db
from models.ingredient import Ingredient
from models.portion import Portion
from models.recipe import Recipe, recipe_ingredient

ingredients = [
  'ice',
  'lime',
  'lemon',
  'orange',
  'salt',
  'pepper',
  'sugar'
]

portions = [
  ['tsp', 'teaspoon'],
  ['tbsp', 'tablespoon'],
  ['fl oz', 'fluid ounce'],
  ['c', 'cup'],
  ['pt', 'pint'],
  ['qt', 'quart'],
  ['gal', 'gallon'],
  ['ml', 'milliliter'],
  ['l', 'liter'],
  ['lb', 'pound'],
  ['oz', 'ounce'],
  ['g', 'gram'],
  ['kg', 'kilogram'],
  ['cm', 'centimeter'],
  ['m', 'meter'],
  ['in', 'inch']
]

def create_ingredient(ingredient_name):
  try:
    ingredient = Ingredient(name=ingredient_name)
    db.session.add(ingredient)
    db.session.commit()
  except:
    db.session.rollback()

for ingredient in ingredients:
  create_ingredient(ingredient)



def create_portion(portion_data):
  try:
    portion = Portion(portion_data[1], portion_data[0])
    db.session.add(portion)
    db.session.commit()
  except:
    db.session.rollback()

for portion in portions:
    create_portion(portion)
