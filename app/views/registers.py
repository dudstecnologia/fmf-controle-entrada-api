from app import db
from flask import request, jsonify
from ..models.registers import Registers, register_schema, registers_schema

def register_entry(user):
    request_data = request.get_json()

    if 'plate' in request_data:
        plate = request_data['plate']
    else:
        return jsonify({'message': 'A placa do veículo é obrigatório', 'data': {}}), 400

    register = Registers(user.id, plate)

    try:
        db.session.add(register)
        db.session.commit()

        return jsonify({'message': 'Entrada registrada com sucesso', 'data': {}}), 201
    except:
        return jsonify({'message': 'Ocorreu um erro ao registrar a entrada', 'data': {}}), 400
