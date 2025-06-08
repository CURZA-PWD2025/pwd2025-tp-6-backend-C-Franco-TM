from app.database.conect_db import get_connection

class ProveedorModel:
    def __init__(self, id, nombre, telefono, direccion, email):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.email = email

    def serializar(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'telefono': self.telefono,
            'direccion': self.direccion,
            'email': self.email
        }

    @staticmethod
    def deserializar(data):
        return ProveedorModel(
            id=data.get('id'),
            nombre=data['nombre'],
            telefono=data['telefono'],
            direccion=data['direccion'],
            email=data['email']
        )

    @staticmethod
    def get_all():
        connection = get_connection()
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM PROVEEDORES")
            rows = cursor.fetchall()
        connection.close()
        return [ProveedorModel(**row).serializar() for row in rows]

    @staticmethod
    def get_one(id):
        connection = get_connection()
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM PROVEEDORES WHERE id = %s", (id,))
            row = cursor.fetchone()
        connection.close()
        if row:
            return ProveedorModel(**row)
        return None

    def create(self):
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO PROVEEDORES (nombre, telefono, direccion, email) VALUES (%s, %s, %s, %s)",
                (self.nombre, self.telefono, self.direccion, self.email)
            )
            connection.commit()
        connection.close()

    def update(self):
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE PROVEEDORES SET nombre = %s, telefono = %s, direccion = %s, email = %s WHERE id = %s",
                (self.nombre, self.telefono, self.direccion, self.email, self.id)
            )
            connection.commit()
        connection.close()

    @staticmethod
    def delete(id):
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM PROVEEDORES WHERE id = %s", (id,))
            connection.commit()
        connection.close()
