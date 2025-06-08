from flask import Blueprint, jsonify, request
from app.proveedor.proveedor_controller import ProveedorController

proveedor_bp = Blueprint('proveedor_bp', __name__, url_prefix='/proveedores')

@proveedor_bp.route('/', methods=['GET'])
def get_all_proveedores():
    return jsonify(ProveedorController.get_all())

@proveedor_bp.route('/<int:id>', methods=['GET'])
def get_proveedor(id):
    return jsonify(ProveedorController.get_one(id))

@proveedor_bp.route('/', methods=['POST'])
def create_proveedor():
    data = request.json
    return jsonify(ProveedorController.create(data))

@proveedor_bp.route('/<int:id>', methods=['PUT'])
def update_proveedor(id):
    data = request.json
    data['id'] = id
    return jsonify(ProveedorController.update(data))

@proveedor_bp.route('/<int:id>', methods=['DELETE'])
def delete_proveedor(id):
    return jsonify(ProveedorController.delete(id))
