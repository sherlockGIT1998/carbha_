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
        
        price = PuneHouseData(area_type,availability,size,total_sqft,bath,balcony,site_location)
        
        predict = price.get_predicted_price()
        
        return f'Price of Pune House is : Rs. {round(predict,2)} Lakh/-'