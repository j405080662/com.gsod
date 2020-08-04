import  pymysql

#
# conn1 = MySQLdb.connect('localhost','pythonweb','19980521','pass',charset='utf8')


def getLoc():
        conn = pymysql.connect('localhost', 'root', '405080662', 'test', charset='utf8')
        cul = conn.cursor()
        sql = 'select stn,wban,latitude,longitude from {0} '.format('gso')
        cul.execute(sql)
        res = cul.fetchall()
        cul.close()
        return res
