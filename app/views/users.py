from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
from ..models.users import Users, user_schema, users_schema

def user_by_email(email):
    try:
        return Users.query.filter(Users.email == email).one()
    except:
        return None

def user_data(user):
    result = user_schema.dump(user)
    return jsonify({ 'data': result }), 200

def register():
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    type = request.json['type']

    user = user_by_email(email)
    if user:
        return jsonify({'message': 'O e-mail informado já está cadastrado', 'data': {}}), 400

    password = generate_password_hash(password)
    user = Users(name, email, password, type)

    try:
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)

        return jsonify({ 'message': 'Usuário registrado com sucesso', 'data': result }), 201
    except:
        return jsonify({ 'message': 'Ocorreu um erro ao registrar o usuário', 'data': {} }), 400
