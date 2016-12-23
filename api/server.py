import sys 

from app import app

from app.routes.ingredient import ingredient_index, ingredient_category, ingredient_all, ingredient_create
from app.routes.recipe import recipe_index, recipe_all, recipe_create

if (sys.argv[1] == "run"):
  app.run(debug=True, use_reloader=False)

if (sys.argv[1] == "create"):
  # TODO: Create the database
  pass

if (sys.argv[1] == "seed"):
  # TODO: Seed the database
  pass 
 
