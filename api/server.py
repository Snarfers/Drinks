from api import app

from routes.ingredient import ingredient_index, ingredient_category, ingredient_all, ingredient_create
from routes.recipe import recipe_index, recipe_all, recipe_create

if __name__ == '__main__':
    app.run(debug=True)
