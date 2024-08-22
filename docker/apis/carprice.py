import joblib
import pandas as pd
import numpy as np


# Add logging

def predictPrice(carlength, carwidth, horsepower, brandavg, averagempg):
    try:
        model = joblib.load("/home/ravikumar/wslgit/ML_playground/docker/models/carprice.joblib")
                
        X_submit = pd.DataFrame({
            'carlength': [float(carlength)],
            'carwidth': [float(carwidth)],
            'horsepower': [float(horsepower)],
            'brandavg': [float(brandavg)],
            'averagempg': [float(averagempg)]
        })
        predicted_price = 10**model.predict(X_submit)[0]
        return int(predicted_price)
    except Exception as e:
        raise e
print(predictPrice(140,30,110,12,10))