from app import db

#Association Tables
recipe_recipeIngredient = db.Table('recipe_recipeingredient', db.metadata,
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')),
    db.Column('recipeingredient_id', db.Integer, db.ForeignKey('recipeingredient.id'))
)

class Recipe(db.Model):
  __tablename__ = 'recipe'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True, index=True)
  ingredients = db.relationship('RecipeIngredient', secondary=recipe_recipeIngredient)

  def __repr__(self):
    return '<Ingredient %r>' % self.name

class RecipeIngredient(db.Model):
    __tablename__ = "recipeingredient"
    id = db.Column(db.Integer, primary_key=True)
    ingredient = db.relationship('Ingredient')
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'))
    quantity = db.Column(db.String)
    portion = db.relationship('Portion')
    portion_id = db.Column(db.Integer, db.ForeignKey('portion.id'))
