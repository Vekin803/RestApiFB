import fdb

def Consulta(sql):
    con = fdb.connect( dsn='192.168.1.252:W:\STECCS_MGV.FDB',
                       user='sysdba',
                       password='masterkey',
                       charset='UTF8')
    cur = con.cursor()
    results = cur.execute(sql)
    columns = [column[0] for column in cur.description]
    items = []
    for row in cur.fetchall():
        items.append(dict(zip(columns, row)))
    con.close()
    return items
