import sys

from app import app

from app.routes.ingredient import ingredient_index, ingredient_category, ingredient_all, ingredient_create
from app.routes.recipe import recipe_index, recipe_all, recipe_create

def run_server():
    app.run(debug=True, use_reloader=False)

def seed_database():
    # TODO: Create the database
    pass

def create_database():
    # TODO: Seed the database
    pass

def main():
    if (len(sys.argv) == 1):
        run_server()
    elif (sys.argv[1] == "run"):
        run_server()
    elif (sys.argv[1] == "create"):
        create_database()
    elif (sys.argv[1] == "seed"):
        seed_database()

if __name__ == "__main__":
    main()
