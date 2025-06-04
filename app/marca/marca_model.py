from app.database.conect_db import get_connection

class MarcaModel:
    def __init__(self, id=None, nombre=None):
        self.id = id
        self.nombre = nombre

    def serializar(self):
        return {
            'id': self.id,
            'nombre': self.nombre
        }

    @classmethod
    def get_all(cls):
        connection = get_connection()
        marcas = []
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT id, nombre FROM MARCAS")
            rows = cursor.fetchall()
            for row in rows:
                marca = cls(**row)  # row = {'id': ..., 'nombre': ...}
                marcas.append(marca.serializar())
        connection.close()
        return marcas

    @classmethod
    def get_by_id(cls, id):
        connection = get_connection()
        marca = None
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT id, nombre FROM MARCAS WHERE id = %s", (id,))
            row = cursor.fetchone()
            if row:
                marca = cls(**row)
        connection.close()
        return marca

    def save(self):
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO MARCAS (nombre) VALUES (%s)", (self.nombre,))
            connection.commit()
            self.id = cursor.lastrowid
        connection.close()
        return self

    def update(self):
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("UPDATE MARCAS SET nombre = %s WHERE id = %s", (self.nombre, self.id))
            connection.commit()
        connection.close()

    def delete(self):
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM MARCAS WHERE id = %s", (self.id,))
            connection.commit()
        connection.close()
