from app import db
from models.ingredient import Ingredient, IngredientTag
from models.portion import Portion
from models.recipe import Recipe, RecipeIngredient

db.create_all()


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
  ingredient = Ingredient(name=ingredient_name)
  db.session.add(ingredient)
  db.session.commit()


for ingredient in ingredients:
  create_ingredient(ingredient)

def create_portion(portion_data):
  try:
    portion = Portion(name=portion_data[1], abbrivation=portion_data[0])
    db.session.add(portion)
    db.session.commit()
  except:
    db.session.rollback()

for portion in portions:
    create_portion(portion)


recipe = Recipe(name="LemonLime") #Create a Recipe
r_ingredient = Ingredient.query.filter_by(name="lime").first() #Get the lime ingredient
r_ingredient.tags.append(IngredientTag(key="cost", value="$5")) # The lime costs $5
r_portion = Portion.query.filter_by(name="cup").first() #
recipeIngredient = RecipeIngredient(ingredient=r_ingredient, quantity="half", portion=r_portion)
recipe.ingredients.append(recipeIngredient)

db.session.add(recipe)
db.session.commit()
