import requests

x = requests.get('http://127.0.0.1:5000/zumi/non')
print(x.status_code)
print(x.ok)
print(x.content)