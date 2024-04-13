from flask import Flask, render_template, request
import secrets
import os


app = Flask(__name__)
app.secret_key = secrets.token_hex()


@app.route('/')
def index():
    return render_template('index.html')




if __name__ == '__main__':
    # Se podría ejecutar usando flask run --debug --host=0.0.0.0
    # debug=True para no tener que parar y volver a poner en marcha el servidor si hacemos algún cambio
    debug_mode = True if os.environ.get('DEBUG') == 'True' else False
    app.run(host='0.0.0.0', debug=debug_mode, port=3000)