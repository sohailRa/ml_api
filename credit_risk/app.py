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
