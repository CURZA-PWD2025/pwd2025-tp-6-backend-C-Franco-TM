from app.proveedor.proveedor_model import ProveedorModel

class ProveedorController:

    @staticmethod
    def get_all():
        return ProveedorModel.get_all()

    @staticmethod
    def get_one(id):
        proveedor = ProveedorModel.get_one(id)
        return proveedor.serializar() if proveedor else {}

    @staticmethod
    def create(data):
        proveedor = ProveedorModel.deserializar(data)
        proveedor.create()
        return {'message': 'Proveedor creado correctamente'}

    @staticmethod
    def update(data):
        proveedor = ProveedorModel.deserializar(data)
        proveedor.update()
        return {'message': 'Proveedor actualizado correctamente'}

    @staticmethod
    def delete(id):
        ProveedorModel.delete(id)
        return {'message': 'Proveedor eliminado correctamente'}
