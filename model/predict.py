import pickle
import pandas as pd
import numpy as np
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

pipe = pickle.load(open(os.path.join(BASE_DIR,'model','pipe.pkl'),'rb'))
columns = pickle.load(open(os.path.join(BASE_DIR,'model','columns.pkl'),'rb'))

def predict_price(input_dict):

    query = pd.DataFrame([input_dict])[columns]

    result = pipe.predict(query)[0]

    return int(np.exp(result))