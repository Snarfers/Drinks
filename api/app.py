from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from os.path import isfile

#Initialize the Application
app = Flask(__name__)

#Initialize the Database
db = SQLAlchemy(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///drinks.db"


# CONSTANTS
COMMON = {}
COMMON['SUCCESS'] = {"status": "success", "data": None, "message": None}
COMMON['API_ROUTE'] = "/api"


#Helper Functions
def row_to_dict(row, excludes=set()):
  d = {}

  for column in row.__table__.columns:
    if column.name not in excludes:
      d[column.name] = str(getattr(row, column.name))

  return d
