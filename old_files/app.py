import fdb
from flask import Flask, jsonify, json, render_template
from flask_restful import Api
from flask_cors import CORS
from flask_jwt import JWT

from resources.formaspago import FormasPago
from resources.users import UserName, Login
from security import authenticate, identity

app = Flask('__name__')
app.secret_key = 'mi_clave_secreta'
api = Api(app)
CORS(app)

jwt = JWT(app, authenticate, identity)

@app.route('/')
def main():
    return render_template('login.html')


api.add_resource(Login, '/login')
api.add_resource(FormasPago, '/formaspago/')
api.add_resource(UserName, '/user/<string:username>')

app.run(port=5000, debug=True)
