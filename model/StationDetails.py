from db import connectHive
import pandas as pd
def getDetails(stn,wban):
    data = connectHive.getWindSpeedData(stn,wban)

    m1=[]
    m2=[]
    m3=[]
    m4=[]
    if len(data)==0:
        return data
    for i in data:
        month = (int(i[0][4:6])-1)//3
        if month ==0:
            m1.append(i)
        if month ==1:
            m2.append(i)
        if month ==2:
            m3.append(i)
        if month ==3:
            m4.append(i)
    res=[]
    if len(m1)==0:
        res.append([0,0,0])
    else:
        data = pd.DataFrame(m1)
        mean = data.mean()
        res.append([mean[1],mean[2],mean[3]])
    if len(m1)==0:
        res.append([0,0,0])
    else:
        data = pd.DataFrame(m1)
        mean = data.mean()
        res.append([mean[1], mean[2], mean[3]])
    if len(m2)==0:
        res.append([0,0,0])
    else:
        data = pd.DataFrame(m2)
        mean = data.mean()
        res.append([mean[1], mean[2], mean[3]])
    if len(m3)==0:
        res.append([0,0,0])
    else:
        data = pd.DataFrame(m3)
        mean = data.mean()
        res.append([mean[1], mean[2], mean[3]])
    m1=[]
    m2=[]
    m3=[]
    for i in res:
        m1.append(i[0])
        m2.append(i[1])
        m3.append(i[2])
    return [m1,m2,m3]
# getDetails('007026',99999)

def getChart2(stn,wban):
    data = connectHive.getChart2Data(stn,wban)
    m1 = []
    m2 = []
    m3 = []
    m4 = []
    if len(data) == 0:
        return data
    for i in data:
        month = (int(i[0][4:6]) - 1) // 3
        if month == 0:
            m1.append(i)
        if month == 1:
            m2.append(i)
        if month == 2:
            m3.append(i)
        if month == 3:
            m4.append(i)
    res = []
    if len(m1) == 0:
        res.append([0, 0, 0])
    else:
        data = pd.DataFrame(m1)
        mean = data.mean()
        res.append([mean[1], mean[2]])
    if len(m2) == 0:
        res.append([0, 0, 0])
    else:
        data = pd.DataFrame(m2)
        mean = data.mean()
        res.append([mean[1], mean[2]])
    if len(m3) == 0:
        res.append([0, 0, 0])
    else:
        data = pd.DataFrame(m3)
        mean = data.mean()
        res.append([mean[1], mean[2]])
    if len(m4) == 0:
        res.append([0, 0, 0])
    else:
        data = pd.DataFrame(m4)
        mean = data.mean()
        res.append([mean[1], mean[2]])
    m1 = []
    m2 = []

    for i in res:
        m1.append(i[0])
        m2.append(i[1])
    print(m1)
    print(m2)
    return [m1, m2]

