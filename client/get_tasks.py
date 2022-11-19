import requests
from pprint import pprint

base_url = 'http://127.0.0.1:8000/api/'

r = requests.get(f'{base_url}tasks/')

if r.status_code == 200:
    pprint(r.json())
else:
    print(r.status_code)