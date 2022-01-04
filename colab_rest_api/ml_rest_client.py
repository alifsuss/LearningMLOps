import json
import requests

url = 'http://0b21-34-125-164-19.ngrok.io/predict'

request_data = json.dumps({'age':40,'salary':20000})
response = requests.post(url,request_data)
print (response.text)
