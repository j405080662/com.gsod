from db import mysql
def getStation():
    out = []
    data = mysql.getLoc()

    for i in data:
        item = {'name': str(i[0] + "-" + i[1]), 'value': [i[3], i[2]]}
        out.append(item)
    return out