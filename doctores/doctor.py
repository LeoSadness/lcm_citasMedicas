from unittest import result
import mysql.connector
import datetime
import hashlib
import doctores.conexion as conexion

#llamar la clase conectar

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Doctor:
    def __init__(self, nombre, apellidos, noConsultorio, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.noConsultorio = noConsultorio
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()
        sql = "INSERT INTO doctores VALUES(null, %s, %s, %s, %s, %s, %s)"
        
        #Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        doctor = (self.nombre, self.apellidos, self.noConsultorio, self.email, cifrado.hexdigest(), fecha)

        try:      
            cursor.execute(sql, doctor)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        return result

    def identificar(self):
        # Login de doctores
        sql = "SELECT * FROM doctores WHERE email = %s AND password = %s"

        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        #Datos para una consulta
        doctor = (self.email, cifrado.hexdigest())

        cursor.execute(sql, doctor)
        result = cursor.fetchone()
        
        return result




