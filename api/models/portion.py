from app import db

class Portion(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), unique=True, index=True)
  abbrivation = db.Column(db.String(50), unique=True, index=True)


  def __repr__(self):
    return '<Portion %r>' % self.name
