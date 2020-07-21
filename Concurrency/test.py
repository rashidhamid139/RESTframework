import requests
import json


s = requests.Session()

s.auth = ('user', 'pass')

s.headers.update({'x-test': 'true'})

a = s.get('https://httpbin.org/headers', headers={'x-test2': 'true'})

print(a.text)