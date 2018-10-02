import fdb

class User:

    def __init__(self, username, useremail, clavewp):
        self.username = username
        self.useremail = useremail
        self.clavewp = clavewp


    @classmethod
    def find_by_email(cls, useremail):
        user_email_lower = useremail.lower()

        con = fdb.connect( dsn='192.168.1.252:W:\STECCS_MGV.FDB',
                           user='sysdba',
                           password='masterkey',
                           charset='UTF8')
        cur = con.cursor()

        query = "SELECT NOMBRE, EMAIL1, CLAVE_WP FROM CLIENTES WHERE EMAIL1='{}'".format(user_email_lower)

        result = cur.execute(query)
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        con.close()
        return user


    @classmethod
    def find_by_username(cls, username):
        username_upper = username.upper()

        con = fdb.connect( dsn='192.168.1.252:W:\STECCS_MGV.FDB',
                           user='sysdba',
                           password='masterkey',
                           charset='UTF8')
        cur = con.cursor()

        query = "SELECT NOMBRE, EMAIL1, CLAVE_WP FROM CLIENTES WHERE NOMBRE='{}'".format(username_upper)

        result = cur.execute(query)
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        con.close()
        return user
