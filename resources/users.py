
from flask import request
from flask_restful import Resource

from connect_fdb import Consulta

class Login(Resource):
    def post(self):
        username = request.form['username']
        password = request.form['password']
        user = Consulta("SELECT Nombre, Telefono1, Email FROM CLIENTES WHERE NOMBRE = '{}' AND CLAVE_WP = '{}'".format(username, password))
        if user:
            return { 'user': user }
        else:
            return {'message': 'User no existe'}



class UserName(Resource):
    def get(self, username):
        return Consulta("SELECT NOMBRE, TELEFONO1, EMAIL FROM CLIENTES WHERE NOMBRE = '{}'".format(username))

    def post(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
