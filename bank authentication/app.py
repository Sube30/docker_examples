# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 16:44:34 2023

@author: Subetha
"""
#Import libraries
from flask import Flask,request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
#import pickle
pickle_in = open('bank_classifier.pkl','rb')
classifier = pickle.load(pickle_in)

#Welcome page.
@app.route('/')
def welcome():
    return "Hello World"


@app.route('/predict')

def predict_note_authentication():
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    return "The predicted values is"+str(prediction)

@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    df_test = pd.read_csv(request.files.get("file"))
    print(df_test)
    prediction = classifier.predict(df_test)
    return "The prediction file is "+str(list(prediction))













if __name__=='__main__':
    app.run()
