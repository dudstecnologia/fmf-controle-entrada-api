import datetime
from app import db, ma
from marshmallow import fields

class Registers(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    plate = db.Column(db.String(20), nullable=False)
    date_entry = db.Column(db.DateTime, default=datetime.datetime.now())
    date_exit = db.Column(db.DateTime, nullable=True)
    status_delivery = db.Column(db.Integer, default=1)
    status_deliveryman = db.Column(db.Integer, default=1)
    user = db.relationship('Users', back_populates='registers')

    def __init__(self, user_id, plate):
        self.user_id = user_id
        self.plate = plate

class RegistersSchema(ma.Schema):
    id = fields.Integer()
    user_id = fields.Integer()
    plate = fields.Str()
    date_entry = fields.DateTime()
    date_exit = fields.DateTime()
    status_delivery = fields.Integer()
    status_deliveryman = fields.Integer()

register_schema = RegistersSchema()
registers_schema = RegistersSchema(many=True)
