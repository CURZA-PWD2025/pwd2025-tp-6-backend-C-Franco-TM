from app.database.conect_db import get_connection

class CategoriaModel:
    def __init__(self, id, descripcion):
        self.id = id
        self.descripcion = descripcion

    def serializar(self):
        return {
            'id': self.id,
            'descripcion': self.descripcion
        }

    @staticmethod
    def deserializar(data):
        return CategoriaModel(
            id=data.get('id'),
            descripcion=data['descripcion']
        )

    @staticmethod
    def get_all():
        connection = get_connection()
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM CATEGORIAS")
            rows = cursor.fetchall()
        connection.close()
        return [CategoriaModel(**row).serializar() for row in rows]

    @staticmethod
    def get_one(id):
        connection = get_connection()
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM CATEGORIAS WHERE id = %s", (id,))
            row = cursor.fetchone()
        connection.close()
        if row:
            return CategoriaModel(**row)
        return None

    def create(self):
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO CATEGORIAS (descripcion) VALUES (%s)", (self.descripcion,))
            connection.commit()
        connection.close()

    def update(self):
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("UPDATE CATEGORIAS SET descripcion = %s WHERE id = %s", (self.descripcion, self.id))
            connection.commit()
        connection.close()

    @staticmethod
    def delete(id):
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM CATEGORIAS WHERE id = %s", (id,))
            connection.commit()
        connection.close()
