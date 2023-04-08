import datetime
from functools import wraps
from app import app
from flask import request, jsonify
from .users import user_by_email
import jwt
from werkzeug.security import check_password_hash

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('token')
        if not token:
            return jsonify({ 'message': 'O token de autenticação é obrigatório', 'data': [] }), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = user_by_email(data['email'])
        except:
            return jsonify({'message': 'Token inválido', 'data': []}), 401
        return f(current_user, *args, **kwargs)
    return decorated

def auth():
    if not request.data:
        return jsonify({'message': 'Informe email e senha'}), 401

    request_data = request.get_json()
    if 'email' in request_data and 'password' in request_data:
        email = request_data['email']
        password = request_data['password']
    else:
        return jsonify({'message': 'Informe email e senha'}), 401

    user = user_by_email(email)
    if not user:
        return jsonify({ 'message': 'E-mail não encontrado' }), 401

    if user and check_password_hash(user.password, password):
        token = jwt.encode({ 'email': user.email, 'exp': datetime.datetime.now() + datetime.timedelta(hours=24) }, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'message': 'Logado com sucesso', 'token': token,
                        'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})

    return jsonify({ 'message': 'Credenciais inválidas' }), 401
