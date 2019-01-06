import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression

#Loading Data
trainDF = pd.read_csv('lib/data/cs-training.csv', index_col=0)
trainDF = trainDF.dropna()


y = trainDF.SeriousDlqin2yrs
X = trainDF.drop(['SeriousDlqin2yrs'], axis=1)

# lr_clf = LogisticRegression()
lr_clf = LogisticRegression(C= .1, penalty='l1', tol=1e-6)
lr_clf.fit(X,y)
#check accuracy
print ("accuracy is ", lr_clf.score(X,y)) #mult by 100% to get %accuracy

# Saving model by picking
pickle.dump(lr_clf, open('lib/models/model.pkl','wb'), protocol=2)


# print("Testing Predict:\n\n")
# v = X.iloc[[0]]
# print(v)
# print(type(v))

# v_dict = v.to_dict('records')

# req = pd.DataFrame.from_dict(v_dict)
# print(req)
# print(type(req))


# prediction = lr_clf.predict(req)
# pred_proba = lr_clf.predict_proba(req)

# if prediction == 0:
#     result = "Default Negative"
# else:
#     result = "Default Positive"
    
# output = {'prediction': result, 'confidence': pred_proba[0][0]}
# print(output)