from app.marca.marca_model import MarcaModel

class MarcaController:

    @staticmethod
    def get_all():
        return MarcaModel.get_all()

    @staticmethod
    def get_one(id):
        marca = MarcaModel.get_one(id)
        return marca.serializar() if marca else {}

    @staticmethod
    def create(data):
        marca = MarcaModel.deserializar(data)
        marca.create()
        return {'message': 'Marca creada correctamente'}

    @staticmethod
    def update(data):
        marca = MarcaModel.deserializar(data)
        marca.update()
        return {'message': 'Marca actualizada correctamente'}

    @staticmethod
    def delete(id):
        MarcaModel.delete(id)
        return {'message': 'Marca eliminada correctamente'}
