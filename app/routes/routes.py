from app import app
from flask import jsonify
from ..views import users, helper, registers

@app.route('/')
def root():
    return jsonify({'message': 'API - Controle de Entrada'})

@app.route('/auth', methods=['POST'])
def auth():
    return helper.auth()

@app.route('/register', methods=['POST'])
def register():
    return users.register()

@app.route('/user-data', methods=['GET'])
@helper.token_required
def get_user_data(user):
    return users.user_data(user)

@app.route('/register-entry', methods=['POST'])
@helper.token_required
def register_entry(user):
    return registers.register_entry(user)
