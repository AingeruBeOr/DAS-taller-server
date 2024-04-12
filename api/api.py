from fastapi import FastAPI
import database as db
from pydantic import BaseModel


class Cliente(BaseModel):
    nombre: str
    telefono: int
    email: str

class Vehiculo(BaseModel):
    matricula: str
    marca: str
    modelo: str
    nombreCliente: str

class Servicio(BaseModel):
    fecha: str
    descripcion: str
    matricula: str


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id + 5, "q": q}

@app.get("/clients")
def get_clients():
    clients = db.getClients()
    response = []
    for client in clients:
        response.append({
            'nombre': client[0],
            'telefono': client[1],
            'email': client[2],
        })
    return response

@app.get("/vehicles")
def get_vehicles():
    vehicles = db.getVehicles()
    response = []
    for vehicle in vehicles:
        response.append({
            'matricula': vehicle[0],
            'marca': vehicle[1],
            'modelo': vehicle[2],
            'cliente': vehicle[3],
        })
    return response

@app.get("/services")
def get_services():
    services = db.getServices()
    response = []
    for service in services:
        response.append({
            'fecha': service[0],
            'matricula': service[1],
            'descripcion': service[2],
        })
    return response

@app.get("/login")
def login(username: str, password: str):
    if db.userExists(username):
        if db.passwordCorrect(username, password):
            print("Login successful for user: ", username)
            return {"message": "true"}
        else:
            return {"message": "Incorrect password"}
    else:
        return {"message": "User does not exist"}
    
@app.get("/userType")
def userType(username: str):
    return {"message": db.getUserType(username)}

@app.get("/register")
def register(username: str, password: str, tipo: str):
    if db.userExists(username):
        return {"message": "User already exists"}
    else:
        db.createUser(username, password, tipo)
        return {"message": "User created"}

@app.get("/clientsFromUser")
def getClientsFromUser(username: str):
    clientes = db.getClientsFromUser(username)
    response = []
    for cliente in clientes:
        response.append({
            'nombre': cliente[0],
            'telefono': cliente[1],
            'email': cliente[2],
        })
    return response

@app.get("/clientVehicles")
def getClientVehicles(client: str):
    vehiculos = db.getClientVehicles(client)
    response = []
    for vehiculo in vehiculos:
        response.append({
            'matricula': vehiculo[0],
            'marca': vehiculo[1],
            'modelo': vehiculo[2],
            'nombreCliente': vehiculo[3],
        })
    return response

@app.get("/vehicleServices")
def getVehicleServices(matricula: str):
    servicios = db.getVehicleServices(matricula)
    response = []
    for servicio in servicios:
        response.append({
            'fecha': servicio[0],
            'matricula': servicio[1],
            'descripcion': servicio[2],
        })
    return response

@app.post("/addService")
def addService(service: Servicio):
    rowcount = db.insertService(service.fecha, service.matricula, service.descripcion)
    print(rowcount)
    return {"message": "Service added"}

@app.post("/addVehicle")
def addVehicle(vehicle: Vehiculo):
    db.insertVehicle(vehicle.matricula, vehicle.marca, vehicle.modelo, vehicle.nombreCliente)
    return {"message": "Vehicle added"}

@app.post("/addClient")
def addClient(client: Cliente, username: str):
    rowcount = db.insertClient(client.nombre, client.telefono, client.email)
    rowcount2 = db.insertUserClient(username, client.nombre)
    print(rowcount)
    return {"message": "Client added"}