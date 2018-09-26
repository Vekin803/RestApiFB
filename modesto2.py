import fdb
from flask import Flask, jsonify, json
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
        results = cur.execute("select * from FORMAS_DE_PAGO")
        columns = [column[0] for column in cur.description]
        items = []
        for row in cur.fetchall():
            items.append(dict(zip(columns, row)))
        con.close()
        return items

api.add_resource(FormasPago, '/formaspago/')

app.run(port=5000)
