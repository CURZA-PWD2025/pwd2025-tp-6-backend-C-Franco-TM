from app.database.conect_db import ConectDB
from app.marca.marca_model import MarcaModel
from app.proveedor.proveedor_model import ProveedorModel
from app.categoria.categoria_model import CategoriaModel

class ArticuloModel:
    def __init__(self, id, descripcion, precio, stock, marca, proveedor, categorias=None):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca = marca  # MarcaModel
        self.proveedor = proveedor  # ProveedorModel
        self.categorias = categorias if categorias else []

    def serializar(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock": self.stock,
            "marca": self.marca.serializar() if self.marca else None,
            "proveedor": self.proveedor.serializar() if self.proveedor else None,
            "categorias": [c.serializar() for c in self.categorias]
        }

    @staticmethod
    def deserializar(data):
        marca = MarcaModel.get_by_id(data.get("marca", {}).get("id"))
        proveedor = ProveedorModel.get_by_id(data.get("proveedor", {}).get("id"))
        categorias = [CategoriaModel.get_by_id(cat["id"]) for cat in data.get("categorias", [])]

        return ArticuloModel(
            id=data.get("id"),
            descripcion=data.get("descripcion"),
            precio=data.get("precio"),
            stock=data.get("stock"),
            marca=marca,
            proveedor=proveedor,
            categorias=categorias
        )

    @staticmethod
    def get_all():
        cnx = ConectDB.get_connect()
        cursor = cnx.cursor()
        cursor.execute("SELECT id, descripcion, precio, stock, marca_id, proveedor_id FROM ARTICULOS")
        rows = cursor.fetchall()

        articulos = []
        for row in rows:
            id, descripcion, precio, stock, marca_id, proveedor_id = row
            marca = MarcaModel.get_by_id(marca_id)
            proveedor = ProveedorModel.get_by_id(proveedor_id)
            categorias = ArticuloModel.get_categorias_by_articulo_id(id)
            articulo = ArticuloModel(id, descripcion, precio, stock, marca, proveedor, categorias)
            articulos.append(articulo)

        cursor.close()
        cnx.close()
        return articulos

    @staticmethod
    def get_one(id):
        cnx = ConectDB.get_connect()
        cursor = cnx.cursor()
        cursor.execute("SELECT id, descripcion, precio, stock, marca_id, proveedor_id FROM ARTICULOS WHERE id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        cnx.close()

        if row:
            id, descripcion, precio, stock, marca_id, proveedor_id = row
            marca = MarcaModel.get_by_id(marca_id)
            proveedor = ProveedorModel.get_by_id(proveedor_id)
            categorias = ArticuloModel.get_categorias_by_articulo_id(id)
            return ArticuloModel(id, descripcion, precio, stock, marca, proveedor, categorias)
        return None

    def create(self):
        cnx = ConectDB.get_connect()
        cursor = cnx.cursor()
        cursor.execute(
            "INSERT INTO ARTICULOS (descripcion, precio, stock, marca_id, proveedor_id) VALUES (%s, %s, %s, %s, %s)",
            (self.descripcion, self.precio, self.stock, self.marca.id, self.proveedor.id)
        )
        self.id = cursor.lastrowid

        for categoria in self.categorias:
            cursor.execute(
                "INSERT INTO ARTICULOS_CATEGORIAS (articulo_id, categoria_id) VALUES (%s, %s)",
                (self.id, categoria.id)
            )

        cnx.commit()
        cursor.close()
        cnx.close()
        return True

    def update(self):
        cnx = ConectDB.get_connect()
        cursor = cnx.cursor()
        cursor.execute(
            "UPDATE ARTICULOS SET descripcion = %s, precio = %s, stock = %s, marca_id = %s, proveedor_id = %s WHERE id = %s",
            (self.descripcion, self.precio, self.stock, self.marca.id, self.proveedor.id, self.id)
        )
        cursor.execute("DELETE FROM ARTICULOS_CATEGORIAS WHERE articulo_id = %s", (self.id,))
        for categoria in self.categorias:
            cursor.execute(
                "INSERT INTO ARTICULOS_CATEGORIAS (articulo_id, categoria_id) VALUES (%s, %s)",
                (self.id, categoria.id)
            )
        cnx.commit()
        cursor.close()
        cnx.close()
        return True

    @staticmethod
    def delete(id):
        cnx = ConectDB.get_connect()
        cursor = cnx.cursor()
        cursor.execute("DELETE FROM ARTICULOS_CATEGORIAS WHERE articulo_id = %s", (id,))
        cursor.execute("DELETE FROM ARTICULOS WHERE id = %s", (id,))
        cnx.commit()
        cursor.close()
        cnx.close()
        return True

    @staticmethod
    def get_categorias_by_articulo_id(articulo_id):
        cnx = ConectDB.get_connect()
        cursor = cnx.cursor()
        cursor.execute("""
            SELECT C.id, C.nombre
            FROM CATEGORIAS C
            JOIN ARTICULOS_CATEGORIAS AC ON C.id = AC.categoria_id
            WHERE AC.articulo_id = %s
        """, (articulo_id,))
        rows = cursor.fetchall()
        cursor.close()
        cnx.close()
        return [CategoriaModel(id=row[0], nombre=row[1]) for row in rows]
