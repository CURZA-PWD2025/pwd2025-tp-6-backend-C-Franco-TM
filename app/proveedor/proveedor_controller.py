from app.proveedor.proveedor_model import ProveedorModel

class ProveedorController:

    @staticmethod
    def get_all():
        proveedores = ProveedorModel.get_all()
        return [p.serializar() for p in proveedores]

    @staticmethod
    def get_one(id):
        proveedor = ProveedorModel.get_by_id(id)
        if proveedor:
            return proveedor.serializar()
        return {"error": "Proveedor no encontrado"}

    @staticmethod
    def create(data):
        try:
            proveedor = ProveedorModel(
                id=None,
                nombre=data.get("nombre"),
                telefono=data.get("telefono"),
                direccion=data.get("direccion"),
                email=data.get("email")
            )
            success = proveedor.create()
            return {"message": "Proveedor creado correctamente"} if success else {"error": "No se pudo crear"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def update(id, data):
        try:
            proveedor = ProveedorModel(
                id=id,
                nombre=data.get("nombre"),
                telefono=data.get("telefono"),
                direccion=data.get("direccion"),
                email=data.get("email")
            )
            success = proveedor.update()
            return {"message": "Proveedor actualizado correctamente"} if success else {"error": "No se pudo actualizar"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def delete(id):
        try:
            success = ProveedorModel.delete(id)
            return {"message": "Proveedor eliminado correctamente"} if success else {"error": "No se pudo eliminar"}
        except Exception as e:
            return {"error": str(e)}
