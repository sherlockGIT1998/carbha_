import pickle 
import json 
import pandas as pd  
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import config

class PuneHouseData():
    
    def __init__(self,area_type,availability,size,total_sqft,bath,balcony,site_location):
        
        self.availability = availability
        self.total_sqft = total_sqft
        self.bath = bath
        self.balcony = balcony
        self.site_location = site_location
        
        self.area_type_col = 'area_type_' + area_type
        
        self.size_col = 'size_' + size
        
    def load_models(self):
        
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)
            
        with open(config.JSON_FILE_PATH,'r') as f :
            self.save_data = json.load(f)
            
            self.column_names = np.array(self.save_data['column_names'])
            
    def get_predicted_price(self):
        
        self.load_models()
        
        area_type_col_index =  
    