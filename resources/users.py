
from flask_restful import Resource

from connect_fdb import Consulta

class UserName(Resource):
    def get(self, username):
        return Consulta("SELECT NOMBRE, TELEFONO1, EMAIL FROM CLIENTES WHERE NOMBRE = '{}'".format(username))

    def post(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
