from .. import db

ingredient_ingredienttag = db.Table('ingredient_ingredienttag', db.metadata,
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.id')),
    db.Column('ingredienttag_id', db.Integer, db.ForeignKey('ingredienttag.id'))
)


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    subcategory_id = db.Column(db.Integer, db.ForeignKey('subcategory.id'))
    category = db.relationship("Category", back_populates="ingredient")
    subcategory = db.relationship("Subcategory", back_populates="ingredient")

    tags = db.relationship('IngredientTag', secondary=ingredient_ingredienttag)

    def __repr__(self):
        return '<Ingredient %r>' % self.name


class IngredientTag(db.Model):
    __tablename__ = 'ingredienttag'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(100))
    value = db.Column(db.String(100))


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    ingredient = db.relationship("Ingredient", back_populates="category")

    def __repr__(self):
        return '<Category %r>' % self.name


class Subcategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    ingredient = db.relationship("Ingredient", back_populates="subcategory")

    def __repr__(self):
        return '<Subcategory %r>' % self.name