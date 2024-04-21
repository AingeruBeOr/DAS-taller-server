from flask import Flask, render_template, request
import secrets
import os
import requests


app = Flask(__name__)
app.secret_key = secrets.token_hex()


@app.route('/')
def index():
    users = requests.get('http://34.155.61.4/users').json()
    clients = requests.get('http://34.155.61.4/clients').json()
    return render_template('index.html', users=users, clients=clients)


if __name__ == '__main__':
    # Se podría ejecutar usando flask run --debug --host=0.0.0.0
    # debug=True para no tener que parar y volver a poner en marcha el servidor si hacemos algún cambio
    debug_mode = True if os.environ.get('DEBUG') == 'True' else False
    app.run(host='0.0.0.0', debug=debug_mode, port=3000)