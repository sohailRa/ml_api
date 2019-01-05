import requests

# URL
url = 'http://localhost:8888/api'

# Experience value
exp = 3
request = requests.post(url,json={'exp':exp,})
print(request.json())