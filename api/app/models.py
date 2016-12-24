from app import db

# Association Tables
Recipe_Ingredients = db.Table('Ingredients', db.metadata,
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')),
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.id')))

Recipe_Instructions = db.Table('Instructions', db.metadata,
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')),
    db.Column('instruction_id', db.Integer, db.ForeignKey('instruction.id')))

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(500), unique=True, index=True)


#Ingredient Table
class Ingredient(db.Model):
    __tablename__ = 'ingredient'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    cost = db.Column(db.Integer)
    upc = db.Column(db.String(15), unique=True)
    rating = db.Column(db.Integer)


# Recipe Table
class Recipe(db.Model):
    __tablename__ = 'recipe'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, index=True)
    rating = db.Column(db.Integer)
    author = db.Column(db.Integer, db.ForeignKey('user.id'))
    flavor = db.Column(db.Integer, db.ForeignKey('flavor.id'))
    ingredients = db.relationship('Ingredients', secondary=Recipe_Ingredients)
    instructions = db.relationship('Instructions', secondary=Recipe_Instructions)


#Instruction Table
class Instruction(db.Model):
    __tablename__ = 'instruction'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), unique=True, index=True)


# Flavor Table
class Flavor(db.Model):
    __tablename__ = 'flavor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
