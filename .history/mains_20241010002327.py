from flask import Flask,render_template,request

from utils import PuneHouseData

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print('Pune House Price Prediction...')
    return render_template('index.html')

@app.route('/predict_price',methods=['POST','GET'])
def get_price_info():
    
    if request.method == 'GET':
        print('In GET Method')
        
        data = request.form
        