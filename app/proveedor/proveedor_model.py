from app.database.conect_db import ConectDB

class ProveedorModel:
    def __init__(self, id, nombre, telefono, direccion, email):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.email = email

    def serializar(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "email": self.email
        }

    @staticmethod
    def get_by_id(id):
        cnx = ConectDB.get_connect()
        cursor = cnx.cursor()
        cursor.execute("SELECT id, nombre, telefono, direccion, email FROM PROVEEDORES WHERE id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        cnx.close()
        if row:
            return ProveedorModel(*row)
        return None

    @staticmethod
    def get_all():
        cnx = ConectDB.get_connect()
        cursor = cnx.cursor()
        cursor.execute("SELECT id, nombre, telefono, direccion, email FROM PROVEEDORES")
        rows = cursor.fetchall()
        cursor.close()
        cnx.close()
        return [ProveedorModel(*row) for row in rows]

    def create(self):
        cnx = ConectDB.get_connect()
        cursor = cnx.cursor()
        cursor.execute(
            "INSERT INTO PROVEEDORES (nombre, telefono, direccion, email) VALUES (%s, %s, %s, %s)",
            (self.nombre, self.telefono, self.direccion, self.email)
        )
        cnx.commit()
        cursor.close()
        cnx.close()
        return True

    def update(self):
        cnx = ConectDB.get_connect()
        cursor = cnx.cursor()
        cursor.execute(
            "UPDATE PROVEEDORES SET nombre = %s, telefono = %s, direccion = %s, email = %s WHERE id = %s",
            (self.nombre, self.telefono, self.direccion, self.email, self.id)
        )
        cnx.commit()
        cursor.close()
        cnx.close()
        return True

    @staticmethod
    def delete(id):
        cnx = ConectDB.get_connect()
        cursor = cnx.cursor()
        cursor.execute("DELETE FROM PROVEEDORES WHERE id = %s", (id,))
        cnx.commit()
        cursor.close()
        cnx.close()
        return True
