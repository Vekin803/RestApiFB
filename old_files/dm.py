import fdb
import json

def ConsultaSQL(sql):
    con = fdb.connect(host="127.0.0.1", database="C:\STECCS.FDB", user="sysdba", password="masterkey")
    cur = con.cursor()
    rows = cur.execute(sql)
    items = [dict(zip([key[0] for key in cur.description], row)) for row in rows]
    con.close()
    return items
