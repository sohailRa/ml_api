import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression

TEST = False

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

if TEST:
	#Test Model
	req = pd.read_csv('lib/data/req_data.csv', index_col=0)
	req = req.drop(['SeriousDlqin2yrs'], axis=1)
	req = req.dropna()
	bb = req.iloc[0:1] 

	data = []
	data.append(bb)

	for dat in data:
		prediction = lr_clf.predict(dat)
		pred_proba = lr_clf.predict_proba(dat)

		if prediction == 0:
		    result = "Default Negative"
		else:
		    result = "Default Positive"
		    
		output = {'prediction': result, 'confidence': pred_proba[0]}
		print(output)
		print("--------------------------------------------------------------------")

