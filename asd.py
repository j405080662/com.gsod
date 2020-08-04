
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


if __name__ == '__main__':
    app.run()
