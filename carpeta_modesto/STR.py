from flask import Flask
from flask_restful import Api
from

app = Flask(__name__)
api = Api(app) 

import Resources
app.config['SECRET_KEY'] = 'masterkey'


@app.route('/')
def hola():
    return "Seleccione Petición"

api.add_resource(Resources.UserLogin, '/login')
api.add_resource(Resources.ListUsuarios, '/users')


if __name__ == '__main__':
    app.run()
