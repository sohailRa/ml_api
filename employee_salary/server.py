# Create API of ML model using flask

"""
API for ML model using Flask. 

Input: JSON -> from post request
Output: JSON -> ML predicton response
"""

import numpy as np
from flask import Flask, request, jsonify
import pickle

# init flask app
app = Flask(__name__)

# Loading the picked model
model = pickle.load(open('model.pkl','rb'))

@app.route('/api',methods=['POST'])
def predict():
    # Geting the data from the POST request
    data = request.get_json(force=True)

    # Make prediction 
    prediction = model.predict([[np.array(data['exp'])]])
    output = prediction[0]

    return jsonify(output)

if __name__ == '__main__':
    app.run(port=8888, debug=True)