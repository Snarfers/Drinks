from .. import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    ingredient = db.relationship("Ingredient", back_populates="category")

    def __repr__(self):
        return '<Category %r>' % self.name