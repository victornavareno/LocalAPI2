from flask import Flask

app = Flask(__name__)


# recordamos q debug hacia que se actualice automaticamente
# esta api va a correr en el puerto 5000 
if __name__ == '__main__':
    app.run(port=5000, debug=True)