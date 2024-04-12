import mysql.connector

database = mysql.connector.connect(
    host='mysql', # docker-compose service name
    user='root',
    password='DAS2024',
    database='taller'
)

def getClients():
    cursor = database.cursor()
    sql = "SELECT * FROM clientes"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def getVehicles():
    cursor = database.cursor()
    sql = "SELECT * FROM vehiculos"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def getServices():
    cursor = database.cursor()
    sql = "SELECT * FROM servicios"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def userExists(username):
    cursor = database.cursor()
    sql = "SELECT * FROM appUsers WHERE username = %s"
    cursor.execute(sql, (username,))
    result = cursor.fetchall()
    print("Number of rows: ", len(result))
    return len(result) > 0

def passwordCorrect(username, password):
    cursor = database.cursor()
    sql = "SELECT * FROM appUsers WHERE username = %s AND password = %s"
    cursor.execute(sql, (username, password))
    result = cursor.fetchall()
    return len(result) > 0

def createUser(username, password, tipo):
    cursor = database.cursor()
    sql = "INSERT INTO appUsers (username, password, tipo) VALUES (%s, %s, %s)"
    cursor.execute(sql, (username, password, tipo))
    database.commit()
    return cursor.rowcount

def getClientsFromUser(username):
    cursor = database.cursor()
    sql = """SELECT C.nombre, C.teléfono, C.email 
             FROM userClientes, clientes as C 
             WHERE userName = %s AND C.nombre = userClientes.clienteName"""
    cursor.execute(sql, (username,))
    result = cursor.fetchall()
    return result

def getClientVehicles(client):
    cursor = database.cursor()
    sql = "SELECT * FROM vehiculos WHERE nombreCliente = %s"
    cursor.execute(sql, (client,))
    result = cursor.fetchall()
    return result

def getVehicleServices(matricula):
    cursor = database.cursor()
    sql = "SELECT * FROM servicios WHERE matricula = %s"
    cursor.execute(sql, (matricula,))
    result = cursor.fetchall()
    return result

def getUserType(username):
    cursor = database.cursor()
    sql = "SELECT tipo FROM appUsers WHERE username = %s"
    cursor.execute(sql, (username,))
    result = cursor.fetchall()
    return result[0][0]

def insertService(fecha, matricula, descripcion):
    cursor = database.cursor()
    sql = "INSERT INTO servicios (fecha, matricula, descripcion) VALUES (%s, %s, %s)"
    cursor.execute(sql, (fecha, matricula, descripcion))
    database.commit()
    return cursor.rowcount

def insertVehicle(matricula, marca, modelo, nombreCliente):
    cursor = database.cursor()
    sql = "INSERT INTO vehiculos (matricula, marca, modelo, nombreCliente) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (matricula, marca, modelo, nombreCliente))
    database.commit()
    return cursor.rowcount

def insertClient(nombre, telefono, email):
    cursor = database.cursor()
    sql = "INSERT INTO clientes (nombre, teléfono, email) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nombre, telefono, email))
    database.commit()
    return cursor.rowcount

def insertUserClient(username, clientName):
    cursor = database.cursor()
    sql = "INSERT INTO userClientes (userName, clienteName) VALUES (%s, %s)"
    cursor.execute(sql, (username, clientName))
    database.commit()
    return cursor.rowcount