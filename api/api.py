from fastapi import FastAPI
import database as db

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
            return {"message": True}
        else:
            return {"message": "Incorrect password"}
    else:
        return {"message": "User does not exist"}