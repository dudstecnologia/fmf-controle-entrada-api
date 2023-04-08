import datetime
from app import db, ma
from marshmallow import fields

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    type = db.Column(db.Integer, default=1)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, name, email, password, type):
        self.name = name
        self.email = email
        self.password = password
        self.type = type

class UsersSchema(ma.Schema):
    id = fields.Integer()
    name = fields.Str()
    email = fields.Str()
    type = fields.Integer()
    created_on = fields.DateTime()

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)
