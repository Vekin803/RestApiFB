
from flask_restful import Resource

class FormasPago(Resource):
    def get(self):
        return Consulta("select * from FORMAS_DE_PAGO")
