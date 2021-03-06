# Simple Linear Regression to predict employee salary based on experience

import pandas as pd
import pickle
import json

# Importing the dataset
dataset = pd.read_csv('data/Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Accuracy
from sklearn.metrics import explained_variance_score
variance_score = explained_variance_score(y_test, y_pred)
print("Explained Variance Score: ", variance_score)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'), protocol=2)

# Loading model to compare the results
exp = 1.8
model = pickle.load( open('model.pkl','rb'))
print("Salary for ", str(exp), " years of experience",model.predict([[exp]])[0])