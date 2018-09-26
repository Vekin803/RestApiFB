import fdb
from flask import Flask, jsonify, json
from flask_restful import Resource, Api
from connect_fdb import Consulta

app = Flask('__name__')
api = Api(app)


class FormasPago(Resource):
    def get(self):
        return Consulta("select * from FORMAS_DE_PAGO")

class UserName(Resource):
    def get(self):
        return Consulta("select Nombre, Telefono1, Email from CLIENTES")


api.add_resource(FormasPago, '/formaspago/')
api.add_resource(UserName, '/user/')

app.run(port=5000)
