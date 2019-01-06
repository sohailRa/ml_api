import requests
import pandas as pd
from io import StringIO

READ_FROM_FILE = False
# URL
url = 'http://localhost:5000/'

if READ_FROM_FILE:
	pass
	# req = pd.read_csv('lib/data/req_data.csv', index_col=0)
	# req = req.drop(['SeriousDlqin2yrs'], axis=1)
	# req = req.dropna()
	# req = req.iloc[0:1]


import csv
import json

csv_path="lib/data/req_data.csv"



# else:
# 	dat = """SeriousDlqin2yrs,RevolvingUtilizationOfUnsecuredLines,age,NumberOfTime30-59DaysPastDueNotWorse,DebtRatio,MonthlyIncome,NumberOfOpenCreditLinesAndLoans,NumberOfTimes90DaysLate,NumberRealEstateLoansOrLines,NumberOfTime60-89DaysPastDueNotWorse,NumberOfDependents
# 	1,1,0.766126609,45,2,0.802982129,9120,13,0,6,0,2
# 		"""

# files = {'upload_file': csv} 
# response = requests.get(url, files=files)
# print(response)

with open(csv_path, 'r') as f:
    r = requests.get(url, files={'csv_file': f})
    print(r)
    print(r.json())