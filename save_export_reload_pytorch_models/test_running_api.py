import json
import requests

url = 'http://35.184.211.131:8005/model'

request_data = json.dumps({'age': 56, 'salary': 200000})
response = requests.post(url, request_data)

print(response.text)