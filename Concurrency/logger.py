import requests


resp = requests.get('https://api.github.com', timeout=10)
print(resp)