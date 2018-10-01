
from flask_restful import Resource

from connect_fdb import Consulta

class UserName(Resource):
    def get(self):
        return Consulta("select Nombre, Telefono1, Email from CLIENTES")
