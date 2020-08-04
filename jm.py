def getWindSpeedData(stn,wban):
    try:
        conn = connect(host='192.168.59.100', port=10000, auth_mechanism='PLAIN', user='root',
                       password='123456', database='gsod')
        cursor = conn.cursor()
        # 执行查询
        cursor.execute('select yearmoda,wdsp,mxspd,gust from weather where stn ={0} and wban ={1}'.format(str(stn),str(wban)))
        # 将结果放入dataframe中显示
        # cursor.execute('select * from weather limit 0,10')
         # 关闭连接
        res = cursor.fetchall()
        cursor.close()

        return res