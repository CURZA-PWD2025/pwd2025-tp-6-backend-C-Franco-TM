from flask import Blueprint, request, jsonify
from app.articulos.articulo_controller import ArticuloController

articulo_bp = Blueprint('articulo_bp', __name__, url_prefix='/articulos')

@articulo_bp.route('/', methods=['GET'])
def get_all_articulos():
    result = ArticuloController.get_all()
    return jsonify(result)

@articulo_bp.route('/<int:id>', methods=['GET'])
def get_articulo(id):
    result = ArticuloController.get_one(id)
    return jsonify(result)

@articulo_bp.route('/', methods=['POST'])
def create_articulo():
    data = request.json
    result = ArticuloController.create(data)
    return jsonify(result)

@articulo_bp.route('/<int:id>', methods=['PUT'])
def update_articulo(id):
    data = request.json
    data['id'] = id
    result = ArticuloController.update(data)
    return jsonify(result)

@articulo_bp.route('/<int:id>', methods=['DELETE'])
def delete_articulo(id):
    result = ArticuloController.delete(id)
    return jsonify(result)
