from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression
import csv

app = Flask(__name__)
api = Api(app)

#Logistic Regression Model object
lr_clf = LogisticRegression() 

#Loading trained/picked model
with open("lib/models/model.pkl", 'rb') as f:
    lr_clf.clf = pickle.load(f)

# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('request')


class PredictCreditRisk(Resource):
	@app.route('/', methods=["GET"])
	def get():

		# parser = reqparse.RequestParser()
		# # parser.add_argument("query")
		# parser.add_argument('csv_file', location='files')
		# args = parser.parse_args()
		# file_name = args["csv_file"]
		# with open(file_name, "r") as f:
		# 	fc = f.read()
		# 	return fc
		
		# out = pd.read_csv(args["csv_file"], sep=",")

		#----------------------------------------------
		file = request.files['csv_file']	
		file_contents = file.stream.read().decode("utf-8")
		csv_input = csv.reader(file_contents)
		# print(file_contents)
		print(type(file_contents))
		print(csv_input)
		# for row in csv_input:
		#     print(row)

		from pandas.compat import StringIO
		df = pd.read_csv(StringIO(file_contents), index_col=0)
		print(df)
		req = file_contents
		return req
		#----------------------------------------------

		# prediction = lr_clf.predict(req)
		# pred_proba = lr_clf.predict_proba(req)

		# if prediction == 0:
		# 	result = "Default Negative"
		# else:
		# 	result = "Default Positive"

		# output = {'prediction': result, 'confidence': pred_proba[0]}
		# return output


# Routeing the URL to the resource
api.add_resource(PredictCreditRisk, '/')


if __name__ == '__main__':
    app.run(debug=True)