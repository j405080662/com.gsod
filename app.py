
from flask import Flask,render_template,request
import json

app = Flask(__name__)


@app.route('/home')
def hello_d():

    return render_template('index.html')


from model import Station

@app.route('/index')
def hello_world():
    out = Station.getStation()
    return  json.dumps(out, ensure_ascii=False)

from model import StationDetails
@app.route('/toitem',methods=['POST','GET'])
def toitem():
    if request.method=='POST':
        # 获取stn  和 wban
        stn = request.form.get('stn')
        wban = request.form.get('wban')
        data = StationDetails.getDetails(stn,wban)
        return  json.dumps(data, ensure_ascii=False)

@app.route('/chart2',methods=['POST','GET'])
def chart2():
    if request.method=='POST':
        # 获取stn  和 wban
        stn = request.form.get('stn')
        wban = request.form.get('wban')
        data = StationDetails.getChart2(stn,wban)
        return  json.dumps(data, ensure_ascii=False)

if __name__ == '__main__':
    app.run()
