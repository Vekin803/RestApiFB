
from flask_restful import Resource

from connect_fdb import Consulta

class FormasPago(Resource):
    def get(self):
        return Consulta("select * from FORMAS_DE_PAGO")
