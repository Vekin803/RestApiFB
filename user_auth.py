import fdb
from flask_restful import Resource, reqparse


class User(Resource):
    TABLE_NAME = 'CLIENTES'

    def __init__(self, id, email, clavewp):
        self.id = id
        self.email = email
        self.clavewp = clavewp

    @classmethod
    def find_by_username(cls, email):
        connection = fdb.connect( dsn='192.168.1.252:W:\STECCS_MGV_TEST.FDB',
                           user='sysdba',
                           password='masterkey',
                           charset='UTF8')
        cursor = connection.cursor()

        query = "SELECT NOMBRE, EMAIL, CLAVE_WP FROM {table} WHERE EMAIL='{campo}'".format(table=cls.TABLE_NAME, campo=email)
        result = cursor.execute(query)
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, id):
        connection = fdb.connect( dsn='192.168.1.252:W:\STECCS_MGV.FDB',
                           user='sysdba',
                           password='masterkey',
                           charset='UTF8')
        cursor = connection.cursor()

        query = "SELECT NOMBRE, EMAIL, CLAVE_WP FROM {table} WHERE NOMBRE='{campo}'".format(table=cls.TABLE_NAME, campo=id)
        result = cursor.execute(query)
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user
