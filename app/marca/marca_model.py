from app.database.conect_db import ConectDB

class MarcaModel:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def serializar(self):
        return {
            "id": self.id,
            "nombre": self.nombre
        }

    @staticmethod
    def get_by_id(id):
        cnx = ConectDB.get_connect()
        cursor = cnx.cursor()
        cursor.execute("SELECT id, nombre FROM MARCAS WHERE id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        cnx.close()
        if row:
            return MarcaModel(id=row[0], nombre=row[1])
        return None

    @staticmethod
    def get_all():
        cnx = ConectDB.get_connect()
        cursor = cnx.cursor()
        cursor.execute("SELECT id, nombre FROM MARCAS")
        rows = cursor.fetchall()
        cursor.close()
        cnx.close()
        return [MarcaModel(id=row[0], nombre=row[1]) for row in rows]

    def create(self):
        cnx = ConectDB.get_connect()
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO MARCAS (nombre) VALUES (%s)", (self.nombre,))
        cnx.commit()
        cursor.close()
        cnx.close()
        return True

    def update(self):
        cnx = ConectDB.get_connect()
        cursor = cnx.cursor()
        cursor.execute("UPDATE MARCAS SET nombre = %s WHERE id = %s", (self.nombre, self.id))
        cnx.commit()
        cursor.close()
        cnx.close()
        return True

    @staticmethod
    def delete(id):
        cnx = ConectDB.get_connect()
        cursor = cnx.cursor()
        cursor.execute("DELETE FROM MARCAS WHERE id = %s", (id,))
        cnx.commit()
        cursor.close()
        cnx.close()
        return True
