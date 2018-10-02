
from flask_restful import Resource
from flask_jwt import jwt_required

from connect_fdb import Consulta

class FormasPago(Resource):
    @jwt_required()
    def get(self):
        return Consulta("select * from FORMAS_DE_PAGO")
