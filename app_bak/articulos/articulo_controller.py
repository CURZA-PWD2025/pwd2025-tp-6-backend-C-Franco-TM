from app.articulos.articulo_model import ArticuloModel

class ArticuloController:

    @staticmethod
    def get_all():
        return ArticuloModel.get_all()

    @staticmethod
    def get_one(id):
        articulo = ArticuloModel.get_one(id)
        if articulo:
            return articulo
        return {"error": "Artículo no encontrado"}

    @staticmethod
    def create(data):
        try:
            articulo = ArticuloModel.deserializar(data)
            success = articulo.create()
            if success:
                return {"message": "Artículo creado correctamente"}
            else:
                return {"error": "No se pudo crear el artículo"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def update(id, data):
        try:
            data["id"] = id  # importante: agregar el ID al dict
            articulo = ArticuloModel.deserializar(data)
            success = articulo.update()
            if success:
                return {"message": "Artículo actualizado correctamente"}
            else:
                return {"error": "No se pudo actualizar el artículo"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def delete(id):
        try:
            success = ArticuloModel.delete(id)
            if success:
                return {"message": "Artículo eliminado correctamente"}
            else:
                return {"error": "No se pudo eliminar el artículo"}
        except Exception as e:
            return {"error": str(e)}
