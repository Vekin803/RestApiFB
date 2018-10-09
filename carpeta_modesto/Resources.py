from flask_restful import Resource, reqparse
from dm import ConsultaSQL
from flask_jwt_extended import (create_access_token, create_refresh_token,
jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

parser = reqparse.RequestParser()
parser.add_argument('username', help = 'Campo obligatorio', required = True)
parser.add_argument('password', help = 'Campo obligatorio', required = True)

class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()

        res = ConsultaSQL("SELECT COUNT(*) FROM CLIENTES WHERE NOMBRE = '{}'".format(data['username']))
        if res[0].COUNT > 0:
            return {'message': 'El usuario {} ya existe'.format(data['username'])}

        try:
            ConsultaSQL("INSERT INTO CLIENTES (NOMBRE, CLAVE_WP) VALUES ('{}', '{}')".format(data['username'], data['password']))
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])
            return {'message': 'El usuario {} ha sido creado'.format(data['username']), 'access_token': access_token, 'refresh_token': refresh_token}
        except:
            return {'message': 'Se ha producido un error'}, 500

class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = None
        res = ConsultaSQL("SELECT NOMBRE, CLAVE_WP FROM CLIENTES WHERE NOMBRE = '{}'".format(data['username']))

        if res :
            current_user = res[0]

        if not current_user:
            return {'message': 'El usuario {} no existe'.format(data['username'])}

        if current_user['CLAVE_WP'] == data['password']:
            refresh_token = create_refresh_token(identity = data['username'])
            access_token = create_access_token(identity = data['username'])
            return {
                'message': 'Logged in as {}'.format(data.username),
                'access_token': access_token,
                'refresh_token': refresh_token
                }
        else:
            return {'message': 'Credenciales incorrectas'}

class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity = current_user)
        return {'access_token': access_token}

#
#class RevokedTokenModel(db.Model):
#    __tablename__ = 'revoked_tokens'
#    id = db.Column(db.Integer, primary_key = True)
#    jti = db.Column(db.String(120))
#
#        db.session.add(self)
#        def add(self):
#        db.session.commit()
#
#    @classmethod
#    def is_jti_blacklisted(cls, jti):
#        query = cls.query.filter_by(jti = jti).first()
#        return bool(query)
#

#class UserLogin(Resource):
#    def post(self):
#        data = parser.parse_args()
#        usuario = ConsultaSQL("SELECT FIRST 1 NOMBRE, CLAVE_WP FROM CLIENTES WHERE NOMBRE = '{}'".format(data.username))
#        if usuario:
#            return usuario[0]
#        return False

class ListUsuarios(Resource):
    @jwt_required
    def get(self):
         return ConsultaSQL('SELECT FIRST 10 NOMBRE, CLAVE_WP FROM CLIENTES')
