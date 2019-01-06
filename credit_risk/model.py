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


print("Testing Predict:\n\n")
aa = X.iloc[[15]]
# print(v.to_dict(orient='records'))

# v_dict = v.to_dict('records')
# print("-----------------------------------------------\n")
# req = pd.DataFrame.from_dict(v_dict)
# print(req.to_dict(orient='records'))

bb = [{'NumberOfTime60-89DaysPastDueNotWorse': 0.0,
'NumberOfTime30-59DaysPastDueNotWorse': 2.0,
'NumberRealEstateLoansOrLines': 6.0,
'DebtRatio': 0.8029821290000001,
'NumberOfOpenCreditLinesAndLoans': 13.0,
'age': 45.0,
'NumberOfTimes90DaysLate': 0.0,
'NumberOfDependents': 2.0,
'MonthlyIncome': 9120.0,
'RevolvingUtilizationOfUnsecuredLines': 0.7661266090000001}]

bb = pd.DataFrame.from_dict(bb)
data = []
data.append(bb)
data.append(aa)

for dat in data:
	prediction = lr_clf.predict(dat)
	pred_proba = lr_clf.predict_proba(dat)

	if prediction == 0:
	    result = "Default Negative"
	else:
	    result = "Default Positive"
	    
	output = {'prediction': result, 'confidence': pred_proba[0]}
	print(output)
	print("-----------------------------------------------\n\n")

