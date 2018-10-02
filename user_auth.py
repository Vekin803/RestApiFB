import fdb

 class User:
     @classmethod
     def find_by_user(cls, username):
             con = fdb.connect( dsn='192.168.1.252:W:\STECCS_MGV.FDB',
                                user='sysdba',
                                password='masterkey',
                                charset='UTF8')
             cur = con.cursor()

             email_lower = lowercase(username)

             query = 'SELECT * FROM CLIENTES WHERE username=?'
             result = cur.execute(query, (username,))
             row = result.fetchone()
             if row:
                 user = cls(row[0])
             else:
                 user = None

             con.close()
             return users

     @classmethod
     def find_by_id(cls, _id):
             con = fdb.connect( dsn='192.168.1.252:W:\STECCS_MGV.FDB',
                                user='sysdba',
                                password='masterkey',
                                charset='UTF8')
             cur = con.cursor()

             query = 'SELECT * FROM CLIENTES WHERE id=?'
             result = cur.execute(query, (_id,))
             row = result.fetchone()
             if row:
                 user = cls(row[0])
             else:
                 user = None

             con.close()
             return users
