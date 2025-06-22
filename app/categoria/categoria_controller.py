from app.categoria.categoria_model import CategoriaModel

class CategoriaController:

    @staticmethod
    def get_all():
        categorias = CategoriaModel.get_all()
        return [c.serializar() for c in categorias]

    @staticmethod
    def get_one(id):
        categoria = CategoriaModel.get_by_id(id)
        if categoria:
            return categoria.serializar()
        return {"error": "Categoría no encontrada"}

    @staticmethod
    def create(data):
        try:
            categoria = CategoriaModel(id=None, nombre=data.get("nombre"))
            success = categoria.create()
            return {"message": "Categoría creada correctamente"} if success else {"error": "No se pudo crear"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def update(id, data):
        try:
            categoria = CategoriaModel(id=id, nombre=data.get("nombre"))
            success = categoria.update()
            return {"message": "Categoría actualizada correctamente"} if success else {"error": "No se pudo actualizar"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def delete(id):
        try:
            success = CategoriaModel.delete(id)
            return {"message": "Categoría eliminada correctamente"} if success else {"error": "No se pudo eliminar"}
        except Exception as e:
            return {"error": str(e)}
