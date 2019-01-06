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

