import sys
import json

from app import app, db

from app.routes import index
from app.routes import recipe_create, recipe_list, recipe_find_id, recipe_find_name
from app.routes import ingredient_create, ingredient_list, ingredient_find_id, ingredient_find_name


def run_server():
    app.run(debug=True, use_reloader=False)
    exit()


def create_database():
    db.create_all()
    return


def seed_database():
    # TODO: Create the database
    pass


def main():
    # Default action: run the server
    if (len(sys.argv) == 1):
        run_server()

    # Run the server
    if (sys.argv[1] == "run"):
        run_server()

    # Create the database if it doesn't exist
    if (sys.argv[1] == "create"):
        create_database()

    # Seed the database
    if (sys.argv[1] == "seed"):
        seed_database()


if __name__ == "__main__":
    main()
