from flask import Blueprint, jsonify, request
from app.categoria.categoria_controller import CategoriaController

categoria_bp = Blueprint('categoria_bp', __name__, url_prefix='/categorias')

@categoria_bp.route('/', methods=['GET'])
def get_all_categorias():
    return jsonify(CategoriaController.get_all())

@categoria_bp.route('/<int:id>', methods=['GET'])
def get_categoria(id):
    return jsonify(CategoriaController.get_one(id))

@categoria_bp.route('/', methods=['POST'])
def create_categoria():
    data = request.json
    return jsonify(CategoriaController.create(data))

@categoria_bp.route('/<int:id>', methods=['PUT'])
def update_categoria(id):
    data = request.json
    data['id'] = id
    return jsonify(CategoriaController.update(data))

@categoria_bp.route('/<int:id>', methods=['DELETE'])
def delete_categoria(id):
    return jsonify(CategoriaController.delete(id))
