from app import app
from flask import jsonify
from ..views import users

@app.route('/')
def root():
    return jsonify({'message': 'API - Controle de Entrada'})

@app.route('/register', methods=['POST'])
def register():
    return users.register()
