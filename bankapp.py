# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 10:34:00 2020

@author: Praveen
"""


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from joblib import load

app = Flask(__name__)
model = load('Banking1.save')

@app.route('/')
def home():
    return render_template('Frontend.php')
@app.route('/y_predict',methods=['POST'])
def y_predict():
    x_test = [[int(x) for x in request.form.values()]]
    #print(x_test)
    #job column
    job=[0,0,0,0,0,0,0,0,0,0]
    #admin
    if(x_test[0][1]==3):
        x_test[0].pop(1)
        x_test[0]=job+x_test[0] 
    #technician
    elif(x_test[0][1]==2):
        x_test[0].pop(1)
        job[8]=1
        x_test[0]=job+x_test[0] 
    #services
    elif(x_test[0][1]==4):
        x_test[0].pop(1)
        job[6]=1
        x_test[0]=job+x_test[0]
    #management
    elif(x_test[0][1]==0):
        x_test[0].pop(1)
        job[3]=1
        x_test[0]=job+x_test[0]
    #retired
    elif(x_test[0][1]==5):
        x_test[0].pop(1)
        job[4]=1
        x_test[0]=job+x_test[0]
    #blue-collar
    elif(x_test[0][1]==1):
        x_test[0].pop(1)
        job[0]=1
        x_test[0]=job+x_test[0]
    #unemployed
    elif(x_test[0][1]==8):
        x_test[0].pop(1)
        job[9]=1
        x_test[0]=job+x_test[0]
    #entreprenur
    elif(x_test[0][1]==9):
        x_test[0].pop(1)
        job[1]=1
        x_test[0]=job+x_test[0]
    #housemaid
    elif(x_test[0][1]==10):
        x_test[0].pop(1)
        job[2]=1
        x_test[0]=job+x_test[0]
    #self-employed
    elif(x_test[0][1]==6):
        x_test[0].pop(1)
        job[5]=1
        x_test[0]=job+x_test[0]
    #student
    elif(x_test[0][1]==7):
        x_test[0].pop(1)
        job[7]=1
        x_test[0]=job+x_test[0]
    #martial status column
    mar=[0,0]
    #married
    if(x_test[0][11]==0):
        x_test[0].pop(11)
        mar[0]=1
        x_test[0]=mar+x_test[0]
    #single
    elif(x_test[0][11]==1):
        x_test[0].pop(11)
        mar[1]=1
        x_test[0]=mar+x_test[0]
    #divorced
    elif(x_test[0][11]==2):
        x_test[0].pop(11)
        x_test[0]=mar+x_test[0]
    #education column
    edu=[0,0]
    #secondary
    if(x_test[0][13]==1):
        x_test[0].pop(13)
        edu[0]=1
        x_test[0]=edu+x_test[0]
    #tertiary
    elif(x_test[0][13]==2):
        x_test[0].pop(13)
        edu[1]=1
        x_test[0]=edu+x_test[0]
    #primary
    elif(x_test[0][13]==0):
        x_test[0].pop(13)
        x_test[0]=edu+x_test[0]
    #default column
    if(x_test[0][15]==0):
        x_test[0][15]=0
    else:
        x_test[0][15]=1
    #housing column
    if(x_test[0][17]==0):
        x_test[0][17]=0
    else:
        x_test[0][17]=1
    #loan
    if(x_test[0][18]==0):
        x_test[0][18]=0
    else:
        x_test[0][18]=1
    print(x_test)
    prediction = model.predict(x_test)
    print(prediction)
    output=prediction[0]
    if(output==1):
        return render_template('Frontend.php', prediction_text="He/She will Deposit the Amount")
    else:
        return render_template('Frontend.php',prediction_text="He/She won't Deposit the Amount")

if __name__ == "__main__":
    app.run(debug=True)