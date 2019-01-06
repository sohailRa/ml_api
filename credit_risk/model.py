import pandas as pd
import pickle
from pandas import Series,DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from sklearn.svm import SVC, LinearSVC
from sklearn.linear_model import Perceptron
from sklearn.grid_search import GridSearchCV

from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics


#Learning curve
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import validation_curve

#Loading Data
trainDF = pd.read_csv('lib/data/cs-training.csv', index_col=0)
trainDF = trainDF.dropna()


y = trainDF.SeriousDlqin2yrs
X = trainDF.drop(['SeriousDlqin2yrs'], axis=1)

# regressor = LogisticRegression()
regressor = LogisticRegression(C= .1, penalty='l1', tol=1e-6)
regressor.fit(X,y)
#check accuracy
print ("accuracy is ", regressor.score(X,y)) #mult by 100% to get %accuracy

# Saving model by picking
pickle.dump(regressor, open('lib/models/model.pkl','wb'), protocol=2)