from api import db

from api.models.portion import Portion
from api.models.ingredient import Ingredient, Category, Subcategory

db.create_all()

ingredients = [
    {'name': 'ice', 'category': 'common', 'subcategory': 'frozen'},
    {'name': 'lime', 'category': 'fruit', 'subcategory': 'sour'},
    {'name': 'lemon', 'category': 'fruit', 'subcategory': 'sour'},
    {'name': 'orange', 'category': 'fruit', 'subcategory': 'sweet'},
    {'name': 'salt', 'category': 'common', 'subcategory': 'additive'},
    {'name': 'pepper', 'category': 'common', 'subcategory': 'additive'},
    {'name': 'sugar', 'category': 'common', 'subcategory': 'additive'},
    {'name': 'whiskey', 'category': 'liquor', 'subcategory': 'bourbon'}
]

portions = [
    {'name': 'teaspoon', 'abbreviation': 'tsp'},
    {'name': 'tablespoon', 'abbreviation': 'tbsp'},
    {'name': 'fluid ounce', 'abbreviation': 'fl oz'},
    {'name': 'cup', 'abbreviation': 'c'},
    {'name': 'pint', 'abbreviation': 'pt'},
    {'name': 'quart', 'abbreviation': 'qt'},
    {'name': 'gal', 'abbreviation': 'gl'},
    {'name': 'milliliter', 'abbreviation': 'milliliter'},
    {'name': 'liter', 'abbreviation': 'l'},
    {'name': 'pound', 'abbreviation': 'lb'},
    {'name': 'ounce', 'abbreviation': 'oz'},
    {'name': 'gram', 'abbreviation': 'g'},
    {'name': 'kilogram', 'abbreviation': 'kg'},
    {'name': 'centimeter', 'abbreviation': 'cm'},
    {'name': 'meter', 'abbreviation': 'm'},
    {'name': 'inch', 'abbreviation': 'in'}
]

# Seed Ingredients
for ingredient in ingredients:
    if not Ingredient.query.filter_by(name=ingredient['name']).first():
        ingredient_add = Ingredient(name=ingredient['name'])

        if not Category.query.filter_by(name=ingredient['category']).first():
            category_add = Category(name=ingredient['category'])
            db.session.add(category_add)

        if not Subcategory.query.filter_by(name=ingredient['subcategory']).first():
            subcategory_add = Category(name=ingredient['subcategory'])
            db.session.add(subcategory_add)

        ingredient_add.category = Category.query.filter_by(name=ingredient['category']).first()
        ingredient_add.subcategory = Subcategory.query.filter_by(name=ingredient['subcategory']).first()

        db.session.add(ingredient_add)
        print('Adding', ingredient['name'])
    else:
        print('Ignoring', ingredient['name'])

# Seed Portions
for portion in portions:
    if not Portion.query.filter_by(name=portion['name']).first():
        portion_create = Portion(**portion)
        db.session.add(portion_create)
        print('Adding', portion['name'])
    else:
        print('Ignoring', portion['name'])


db.session.commit()


