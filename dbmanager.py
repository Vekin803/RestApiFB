import fdb


def ConsultaSQL(sql):
    con = fdb.connect( dsn='192.168.1.252:W:\STECCS_MGV_TEST.FDB',
                       user='sysdba',
                       password='masterkey',
                       charset='UTF8')
    cur = con.cursor()
    rows = cur.execute(sql)
    items = [dict(zip([key[0] for key in cur.description], row)) for row in rows]
    con.close()
    return items
