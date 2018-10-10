from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)

import Resources

app.config['JWT_SECRET_KEY'] = 'masterkey'
#app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

#
#@jwt.token_in_blacklist_loader
#def check_if_token_in_blacklist(decrypted_token):
#    jti = decrypted_token['jti']
#    return models.RevokedTokenModel.is_jti_blacklisted(jti)
#

jwt = JWTManager(app)

@app.route('/')
def hola():
    return "Seleccione Petición"

api.add_resource(Resources.UserLogin, '/api/login')
api.add_resource(Resources.ListUsuarios, '/users')


if __name__ == '__main__':
    app.run()
