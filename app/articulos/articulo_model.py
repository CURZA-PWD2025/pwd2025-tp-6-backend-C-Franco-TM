from app.database.conect_db import get_connection
from app.categoria.categoria_model import CategoriaModel

class ArticuloModel:
    def __init__(self, id, descripcion, precio, stock, marca_id, proveedor_id, categorias=None):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca_id = marca_id
        self.proveedor_id = proveedor_id
        self.categorias = categorias if categorias else []

    def serializar(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock": self.stock,
            "marca_id": self.marca_id,
            "proveedor_id": self.proveedor_id,
            "categorias": [c.serializar() for c in self.categorias]
        }

    @staticmethod
    def deserializar(data):
        categorias = [CategoriaModel(**c) for c in data.get("categorias", [])]
        return ArticuloModel(
            id=data.get("id"),
            descripcion=data.get("descripcion"),
            precio=data.get("precio"),
            stock=data.get("stock"),
            marca_id=data.get("marca_id"),
            proveedor_id=data.get("proveedor_id"),
            categorias=categorias
        )

    @staticmethod
    def get_all():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM ARTICULOS")
        rows = cursor.fetchall()
        articulos = []
        for row in rows:
            articulo = ArticuloModel(*row)
            articulo.categorias = ArticuloModel.get_categorias_by_articulo_id(articulo.id)
            articulos.append(articulo)
        cursor.close()
        connection.close()
        return [a.serializar() for a in articulos]

    @staticmethod
    def get_one(id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM ARTICULOS WHERE id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        connection.close()
        if row:
            articulo = ArticuloModel(*row)
            articulo.categorias = ArticuloModel.get_categorias_by_articulo_id(id)
            return articulo.serializar()
        return {}

    def create(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO ARTICULOS (descripcion, precio, stock, marca_id, proveedor_id) VALUES (%s, %s, %s, %s, %s)",
            (self.descripcion, self.precio, self.stock, self.marca_id, self.proveedor_id)
        )
        self.id = cursor.lastrowid

        for categoria in self.categorias:
            cursor.execute(
                "INSERT INTO ARTICULOS_CATEGORIAS (articulo_id, categoria_id) VALUES (%s, %s)",
                (self.id, categoria.id)
            )
        connection.commit()
        cursor.close()
        connection.close()
        return True

    def update(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE ARTICULOS SET descripcion = %s, precio = %s, stock = %s, marca_id = %s, proveedor_id = %s WHERE id = %s",
            (self.descripcion, self.precio, self.stock, self.marca_id, self.proveedor_id, self.id)
        )
        cursor.execute(
            "DELETE FROM ARTICULOS_CATEGORIAS WHERE articulo_id = %s", (self.id,)
        )
        for categoria in self.categorias:
            cursor.execute(
                "INSERT INTO ARTICULOS_CATEGORIAS (articulo_id, categoria_id) VALUES (%s, %s)",
                (self.id, categoria.id)
            )
        connection.commit()
        cursor.close()
        connection.close()
        return True

    @staticmethod
    def delete(id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM ARTICULOS_CATEGORIAS WHERE articulo_id = %s", (id,))
        cursor.execute("DELETE FROM ARTICULOS WHERE id = %s", (id,))
        connection.commit()
        cursor.close()
        connection.close()
        return True

    @staticmethod
    def get_categorias_by_articulo_id(articulo_id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT C.id, C.nombre
            FROM CATEGORIAS C
            JOIN ARTICULOS_CATEGORIAS AC ON C.id = AC.categoria_id
            WHERE AC.articulo_id = %s
        """, (articulo_id,))
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        return [CategoriaModel(id=row[0], nombre=row[1]) for row in rows]
