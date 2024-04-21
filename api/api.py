from fastapi import FastAPI, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import firebase_admin.messaging
import database as db
from pydantic import BaseModel
import firebase_admin
from firebase_admin import credentials
import fcm
import os
from datetime import datetime
import matplotlib.pyplot as plt
import math


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


if not os.path.exists('./documentaciones'): os.mkdir('./documentaciones')
if not os.path.exists('./static/widgetPlots'): os.mkdir('./static/widgetPlots')

app = FastAPI()
app.mount("/documentaciones", StaticFiles(directory="documentaciones"), name="documentaciones")
app.mount("/widgetPlots", StaticFiles(directory="static/widgetPlots"), name="widgetPlots")

# Firebase configuration
cred = credentials.Certificate("das-android-firebase-adminsdk.json")
default_app = firebase_admin.initialize_app(credential=cred)            # Set the service account

# Middleware para permitir solicitudes desde el origen de la aplicación web
origins = [
    "http://34.155.61.4:3000",  # Permitir solicitudes desde este origen
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.get("/users")
def get_users():
    users = db.getUsers()
    response = []
    for user in users:
        response.append({
            'username': user[0],
            'password': user[1],
            'tipo': user[2],
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
def addService(service: Servicio, taller: str):
    rowcount = db.insertService(service.fecha, service.matricula, service.descripcion)
    print(rowcount)
    updateWidgetPlot(taller)
    return {"message": "Service added"}

@app.post("/addVehicle")
def addVehicle(vehicle: Vehiculo):
    db.insertVehicle(vehicle.matricula, vehicle.marca, vehicle.modelo, vehicle.nombreCliente)
    return {"message": "Vehicle added"}

@app.post("/addClient")
def addClient(client: Cliente, username: str, latitude: str, longitude: str):
    rowcount = db.insertClient(client.nombre, client.telefono, client.email, latitude, longitude)
    rowcount2 = db.insertUserClient(username, client.nombre)
    print(rowcount)
    return {"message": "Client added"}

@app.get("/userClient")
def insertUserClient(username: str, clientName: str):
    rowcount = db.insertUserClient(username, clientName)
    return {"message": "User-Client relationship added"}

@app.post("/FCMdevice")
def addFCMtoken(token: str):
    if db.FCMtokenExists(token):
        print("Token already exists: ", token)
        return {"message": "Token already exists"}
    else: 
        rowcount = db.insertFCMtoken(token)
        print("New token added: ", token)
        return {"message": "Token added"}
    

@app.get("/messageToEveryone")
def send_message_to_everyone():
    fcm.send_messages_to_everyone()
    return {"message": "Message sent"}

@app.post("/vehicleDocumentation")
async def vehicleDocumentation(matricula: str, image: UploadFile):
    content = await image.read()
    with open(f"documentaciones/{image.filename}", "wb") as file:
        file.write(content)
    print(f"File type {image.content_type}")
    print(f"Adding {image.filename} to {matricula} vehicle with size {len(content)} bytes")
    db.insertVehicleDocumentation(matricula, image.filename)
    return {"message": "Document added"}

@app.get("/vehicleHasDocumentation")
def vehicleHasDocumentation(matricula: str):
    print(f"Checking if {matricula} has documentation")
    path = db.getVehicleDocumentationPath(matricula)
    if path == None: return {"message": "false"}
    else: return {"message": "true"}

@app.get("/getVehicleDocumentation")
def getVehicleDocumentation(matricula: str):
    documentacionPath = db.getVehicleDocumentationPath(matricula)
    return FileResponse(f"documentaciones/{documentacionPath}")

@app.delete("/deleteVehicle")
def deleteVehicle(matricula: str):
    db.deleteVehicle(matricula)
    return {"message": "Vehicle deleted"}

@app.delete("/deleteClient")
def deleteClient(nombre: str):
    db.deleteCliente(nombre)
    return {"message": "Client deleted"}

@app.delete("/deleteService")
def deleteService(fecha: str, matricula: str, taller: str):
    rowcount = db.deleteService(fecha, matricula)
    updateWidgetPlot(taller)
    return {"message": f"Service deleted. New graph in http://34.155.61.4/widgetPlots/{taller}.png"}

@app.get("/generateWidgetGraph")
def generateWidgetGraph(taller: str):
    updateWidgetPlot(taller)
    return {"message": f"http://34.155.61.4/widgetPlots/{taller}.png"}

def updateWidgetPlot(taller: str):
    result = db.getTallerServices(taller)
    result = [date_list[0] for date_list in result]
    counts = monthResults(result)
    barPlot(counts, taller)
    print(f'{taller}\'s plot updated')

def monthResults(results):
    diction = {
        'current': 0,
        '-1': 0,
        '-2': 0
    }

    current_month, current_year = datetime.now().month, datetime.now().year
    p_month, p_year = getPreviousMonthAndYearTo(current_month, current_year)
    pp_month, pp_year = getPreviousMonthAndYearTo(p_month, p_year)

    for result in results:
        date = datetime.strptime(result, "%d/%m/%Y")
        if date.month == current_month and date.year == current_year:
            diction['current'] += 1
        elif date.month == p_month and date.year == p_year:
            diction['-1'] += 1
        elif date.month == pp_month and date.year == pp_year:
            diction['-2'] += 1
    return diction

def getPreviousMonthAndYearTo(month, year):
    if month == 1:
        return 12, year - 1
    else:
        return month - 1, year

def barPlot(counts, taller):
    current_month, current_year = datetime.now().month, datetime.now().year
    p_month, p_year = getPreviousMonthAndYearTo(current_month, current_year)
    pp_month, _ = getPreviousMonthAndYearTo(p_month, p_year)

    months = [str(pp_month), str(p_month), str(current_month) + ' (Actual)']
    values = [counts['-2'], counts['-1'], counts['current']]
    y_ticks = range(0, math.ceil(max(values) + 1))
    plt.figure(figsize=(2, 4))
    plt.yticks(y_ticks)
    plt.bar(months, values, width = 0.5)
    plt.savefig(f'./static/widgetPlots/{taller}.png')

@app.get("/clientsLocations")
def getClientsLocations(user: str):
    clientLocations = db.getClientsLocations(user)
    clientLocations = [
        {
            'nombre': client[0],
            'latitude': client[1],
            'longitude': client[2],
        }
        for client in clientLocations
    ]
    return clientLocations
