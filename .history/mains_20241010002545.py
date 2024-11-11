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
        area_type = data['area_type']
        availability = data['availability']
        size = data['size']
        total_sqft = data['total_sqft']
        bath = eval(data['bath'])
        balcony = eval(data['balcony'])
        site_location = eval(data['site_location'])