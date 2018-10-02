import fdb
from flask import Flask, jsonify, json
from flask_restful import Api
from flask_cors import CORS
# from flask_jwt import JWT, jwt_required

from resources.formaspago import FormasPago
from resources.users import UserName
from security import authenticate, identity


app = Flask('__name__')
app.secret_key = 'mi_clave_secreta'
api = Api(app)
CORS(app)

jwt = JWT(app, authenticate, identity)


api.add_resource(FormasPago, '/formaspago/')
api.add_resource(UserName, '/user/<string:username>')

app.run(port=5000)
