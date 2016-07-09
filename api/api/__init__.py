from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the Application
app = Flask(__name__)

# Application configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///drinks.db"

# Initialize the Database
db = SQLAlchemy(app)

# CONSTANTS
COMMON = dict()
COMMON['SUCCESS'] = {"status": "success", "data": None, "message": None}
COMMON['DEBUG'] = True


def row_to_dict(row, excludes=set()):
    d = {}

    for column in row.__table__.columns:
        if column.name not in excludes:
            d[column.name] = str(getattr(row, column.name))

    return d