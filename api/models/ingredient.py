from app import db

class Ingredient(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), unique=True)
  
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return '<Ingredient %r>' % self.name