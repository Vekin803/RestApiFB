
from flask import request, jsonify
from flask_restful import Resource

from connect_fdb import Consulta

class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        user = Consulta("SELECT Nombre, Telefono1, Email FROM CLIENTES WHERE NOMBRE = '{}' AND CLAVE_WP = '{}'".format(username, password))
        if user:
            return jsonify(user)
        else:
            return None



class UserName(Resource):
    def get(self, username):
        return Consulta("SELECT NOMBRE, TELEFONO1, EMAIL FROM CLIENTES WHERE NOMBRE = '{}'".format(username))

    def post(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
