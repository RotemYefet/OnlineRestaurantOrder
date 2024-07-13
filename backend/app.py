from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS= CORS(app, origins="*")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

db = SQLAlchemy(app)

from routes import *

with app.app_context():
    db.create_all()
    print("db created" + "\n")
    item_to_create = { "item_name":"pasta", 
                "item_type":"food",
                 "item_price":"15$"}
    item_created = itemHandler.createItemDB(item_to_create)

