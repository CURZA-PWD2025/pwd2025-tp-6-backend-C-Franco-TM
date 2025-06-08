from flask import Blueprint, jsonify, request
from app.marca.marca_controller import MarcaController

marca_bp = Blueprint('marca_bp', __name__, url_prefix='/marcas')

@marca_bp.route('/', methods=['GET'])
def get_all_marcas():
    return jsonify(MarcaController.get_all())

@marca_bp.route('/<int:id>', methods=['GET'])
def get_marca(id):
    return jsonify(MarcaController.get_one(id))

@marca_bp.route('/', methods=['POST'])
def create_marca():
    data = request.json
    return jsonify(MarcaController.create(data))

@marca_bp.route('/<int:id>', methods=['PUT'])
def update_marca(id):
    data = request.json
    data['id'] = id
    return jsonify(MarcaController.update(data))

@marca_bp.route('/<int:id>', methods=['DELETE'])
def delete_marca(id):
    return jsonify(MarcaController.delete(id))
