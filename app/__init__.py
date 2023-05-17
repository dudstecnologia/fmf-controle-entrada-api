from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object('config')
db = SQLAlchemy(app)
ma = Marshmallow(app)

from .models import users, registers
from .views import users, helper
from .routes import routes

with app.app_context():
    db.create_all()
