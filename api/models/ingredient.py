from api import db
print("in ingredient model")

ingredient_ingredienttag = db.Table('ingredient_ingredienttag', db.metadata,
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.id')),
    db.Column('ingredienttag_id', db.Integer, db.ForeignKey('ingredienttag.id'))
)

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    category = db.Column(db.String(50), nullable=True, index=True)
    subcategory = db.Column(db.String(50), nullable=True)
    tags = db.relationship('IngredientTag', secondary=ingredient_ingredienttag)

    def __repr__(self):
        return '<Ingredient %r>' % self.name


class IngredientTag(db.Model):
    __tablename__ = 'ingredienttag'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(100))
    value = db.Column(db.String(100))
