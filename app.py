#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'FIFA_RFR_model.pkl'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    temp_array = list()
    
    if request.method == 'POST':
        
        
        name = request.form['name'] 
        age = int(request.form['age'])
        ball_skills = float(request.form['ball_skills'])
        defence = float(request.form['defence'])
        mental = float(request.form['mental'])
        passing = float(request.form['passing'])
        physical = float(request.form['physical'])
        shooting = float(request.form['shooting'])
        goalkeeping = float(request.form['goalkeeping'])
    
        
        temp_array = temp_array + [age, ball_skills, defence, mental, passing,physical, shooting, goalkeeping]
        
        data = np.array([temp_array])
        my_prediction = model.predict(data)[0]
        my_prediction= np.exp(my_prediction).round(2)
              
        return render_template('result.html', amt= my_prediction, Name= name)



if __name__ == '__main__':
	app.run(debug=True)


# In[ ]:




