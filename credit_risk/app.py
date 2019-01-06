from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)
api = Api(app)

#Logistic Regression Model object
lr_clf = LogisticRegression() 

#Loading trained/picked model
with open("lib/model/model.pkl", 'rb') as f:
    lr_clf.clf = pickle.load(f)

# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('request')


class PredictCreditRisk(Resource):
    
    def get(self):
        # parsing the request
        args = parser.parse_args()
        req = args['request']
		
		req = json.loads(req)
		req = pd.DataFrame.from_json(req)

		prediction = lr_clf.predict(x)
		pred_proba = lr_clf.predict_proba(x)

		if prediction == 0:
		    result = "Default Negative"
		else:
		    result = "Default Positive"
		    
		output = {'prediction': result, 'confidence': pred_proba[0][0]}
		return output


# Routeing the URL to the resource
api.add_resource(PredictCreditRisk, '/')


if __name__ == '__main__':
    app.run(debug=True)