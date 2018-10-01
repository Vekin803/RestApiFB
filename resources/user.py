
from flask_restful import Resource

class UserName(Resource):
    def get(self):
        return Consulta("select Nombre, Telefono1, Email from CLIENTES")
