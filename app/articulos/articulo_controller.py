from app.articulos.articulo_model import ArticuloModel
from app.marca.marca_model import MarcaModel
from app.proveedor.proveedor_model import ProveedorModel
from app.categoria.categoria_model import CategoriaModel

class ArticuloController:

    @staticmethod
    def get_all():
        return ArticuloModel.get_all()

    @staticmethod
    def get_one(id):
        articulo = ArticuloModel.get_one(id)
        if articulo:
            return articulo.serializar()
        return {"error": "Artículo no encontrado"}

    @staticmethod
    def create(data):
        try:
            marca_data = data.get("marca")
            proveedor_data = data.get("proveedor")
            categorias_data = data.get("categorias", [])

            marca = MarcaModel.get_by_id(marca_data["id"])
            proveedor = ProveedorModel.get_by_id(proveedor_data["id"])
            categorias = [CategoriaModel.get_by_id(c["id"]) for c in categorias_data]

            articulo = ArticuloModel(
                id=None,
                descripcion=data.get("descripcion"),
                precio=data.get("precio"),
                stock=data.get("stock"),
                marca=marca,
                proveedor=proveedor,
                categorias=categorias
            )

            articulo.create()
            return {"message": "Artículo creado correctamente"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def update(id, data):
        try:
            marca_data = data.get("marca")
            proveedor_data = data.get("proveedor")
            categorias_data = data.get("categorias", [])

            marca = MarcaModel.get_by_id(marca_data["id"])
            proveedor = ProveedorModel.get_by_id(proveedor_data["id"])
            categorias = [CategoriaModel.get_by_id(c["id"]) for c in categorias_data]

            articulo = ArticuloModel(
                id=id,
                descripcion=data.get("descripcion"),
                precio=data.get("precio"),
                stock=data.get("stock"),
                marca=marca,
                proveedor=proveedor,
                categorias=categorias
            )

            articulo.update()
            return {"message": "Artículo actualizado correctamente"}
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
