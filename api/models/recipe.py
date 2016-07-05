from app import db

class Recipe(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  ingredients = db.relationship('Ingredient', secondary=recipe_ingredient,
                         backref=db.backref('pages', lazy='dynamic'))
                         
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return '<Ingredient %r>' % self.name


#Association Tables
recipe_ingredient = db.Table('recipe_ingredient', db.Base.metadata,
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')),
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.id'))
)
