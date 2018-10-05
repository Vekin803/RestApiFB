from flask_restful import Resource, reqparse
from dm import ConsultaSQL


parser = reqparse.RequestParser()
parser.add_argument('nombre', help = 'Campo obligatorio', required = True)
parser.add_argument('password', help = 'Campo obligatorio', required = True)

class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        usuario = ConsultaSQL("SELECT FIRST 1 NOMBRE, TELEFONO FROM AGENDA WHERE NOMBRE = '" + data.nombre + "'")
        if usuario:
            return usuario[0]
        return none

class ListUsuarios(Resource):
    def get(self):
         return ConsultaSQL('SELECT TELEFONO, NOMBRE FROM AGENDA')
