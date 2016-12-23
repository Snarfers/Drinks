import sys

from app import app

from app.routes.ingredient import ingredient_index, ingredient_category, ingredient_all, ingredient_create
from app.routes.recipe import recipe_index, recipe_all, recipe_create

def main():
    if (len(sys.argv) == 1):
        app.run(debug=True, use_reloader=False)
    elif (sys.argv[1] == "run"):
        app.run(debug=True, use_reloader=False)
    elif (sys.argv[1] == "create"):
        # TODO: Create the database
        pass
    elif (sys.argv[1] == "seed"):
        # TODO: Seed the database
        pass

if __name__ == "__main__":
    main()
