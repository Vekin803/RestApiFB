
import fdb
from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask('__name__')
api = Api(app)

class FormasPago(Resource):
    def get(self):
        con = fdb.connect( dsn='192.168.1.252:W:\STECCS_MGV.FDB',
                           user='sysdba',
                           password='masterkey',
                           charset='UTF8')
        cur = con.cursor()
        result = cur.execute('select * from FORMAS_DE_PAGO')
        items = []
        for row in result:
            items.append({'Forma Pago': row[0], 'Emitir Recibo': row[1], 'Remesar': row[2]})
        con.close()
        return {'Items': items}

api.add_resource(FormasPago, '/formaspago/')

app.run(port=5000)
