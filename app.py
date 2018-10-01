import fdb
from flask import Flask, jsonify, json
from flask_restful import Api
from flask_cors import CORS

from resources.formaspago import FormasPago
from resources.user import UserName


app = Flask('__name__')
api = Api(app)
CORS(app)


api.add_resource(FormasPago, '/formaspago/')
api.add_resource(UserName, '/user/')

app.run(port=5000)
