import requests
from io import StringIO

# URL and  Sample file path
url = 'http://localhost:5000/'
csv_path="lib/data/req_data.csv"

with open(csv_path, 'r') as f:
    r = requests.get(url, files={'csv_file': f})
    print(r)
    print(r.json())