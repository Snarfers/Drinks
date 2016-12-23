from .. import db

class Subcategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    ingredient = db.relationship("Ingredient", back_populates="subcategory")

    def __repr__(self):
        return '<Subcategory %r>' % self.name