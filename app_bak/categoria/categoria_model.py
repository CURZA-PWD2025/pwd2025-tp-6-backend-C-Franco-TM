from app.database.conect_db import get_connection

class CategoriaModel:
    def __init__(self, id=None, nombre=None):
        self.id = id
        self.nombre = nombre

    def serializar(self):
        return {
            'id': self.id,
            'nombre': self.nombre
        }

    @staticmethod
    def deserializar(data):
        return CategoriaModel(
            id=data.get('id'),
            nombre=data.get('nombre')
        )

    @staticmethod
    def get_all():
        connection = get_connection()
        categorias = []
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT id, nombre FROM CATEGORIAS")
            rows = cursor.fetchall()
            for row in rows:
                categorias.append(CategoriaModel(**row).serializar())
        connection.close()
        return categorias

    @staticmethod
    def get_one(id):
        connection = get_connection()
        categoria = None
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT id, nombre FROM CATEGORIAS WHERE id = %s", (id,))
            row = cursor.fetchone()
            if row:
                categoria = CategoriaModel(**row)
        connection.close()
        return categoria

    def create(self):
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO CATEGORIAS (nombre) VALUES (%s)", (self.nombre,))
            connection.commit()
            self.id = cursor.lastrowid
        connection.close()

    def update(self):
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("UPDATE CATEGORIAS SET nombre = %s WHERE id = %s", (self.nombre, self.id))
            connection.commit()
        connection.close()

    @staticmethod
    def delete(id):
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM CATEGORIAS WHERE id = %s", (id,))
            connection.commit()
        connection.close()
