from app.categoria.categoria_model import CategoriaModel

class CategoriaController:

    @staticmethod
    def get_all():
        return CategoriaModel.get_all()

    @staticmethod
    def get_one(id):
        categoria = CategoriaModel.get_one(id)
        return categoria.serializar() if categoria else {}

    @staticmethod
    def create(data):
        categoria = CategoriaModel.deserializar(data)
        categoria.create()
        return {'message': 'Categoría creada correctamente'}

    @staticmethod
    def update(data):
        categoria = CategoriaModel.deserializar(data)
        categoria.update()
        return {'message': 'Categoría actualizada correctamente'}

    @staticmethod
    def delete(id):
        CategoriaModel.delete(id)
        return {'message': 'Categoría eliminada correctamente'}
