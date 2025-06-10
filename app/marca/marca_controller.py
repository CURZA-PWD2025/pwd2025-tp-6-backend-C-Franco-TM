from app.marca.marca_model import MarcaModel

class MarcaController:

    @staticmethod
    def get_all():
        marcas = MarcaModel.get_all()
        return [m.serializar() for m in marcas]

    @staticmethod
    def get_one(id):
        marca = MarcaModel.get_by_id(id)
        if marca:
            return marca.serializar()
        return {"error": "Marca no encontrada"}

    @staticmethod
    def create(data):
        try:
            marca = MarcaModel(id=None, nombre=data.get("nombre"))
            success = marca.create()
            return {"message": "Marca creada correctamente"} if success else {"error": "No se pudo crear"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def update(id, data):
        try:
            marca = MarcaModel(id=id, nombre=data.get("nombre"))
            success = marca.update()
            return {"message": "Marca actualizada correctamente"} if success else {"error": "No se pudo actualizar"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def delete(id):
        try:
            success = MarcaModel.delete(id)
            return {"message": "Marca eliminada correctamente"} if success else {"error": "No se pudo eliminar"}
        except Exception as e:
            return {"error": str(e)}
