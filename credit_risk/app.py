from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
import pickle
import pandas as pd
from pandas.compat import StringIO
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)
api = Api(app)

#Logistic Regression Model object
lr_clf = LogisticRegression() 

#Loading trained/picked model
with open("lib/models/model.pkl", 'rb') as f:
    lr_clf = pickle.load(f)


class PredictCreditRisk(Resource):

	def get(self):

		file = request.files['csv_file']	
		file_contents = file.stream.read().decode("utf-8")
		df = pd.read_csv(StringIO(file_contents), index_col=0)
		req = df.iloc[0:1]
		req = req.drop(['SeriousDlqin2yrs'], axis=1)
		req = req.dropna()

		prediction = lr_clf.predict(req)
		pred_proba = lr_clf.predict_proba(req)

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