import requests

while True:
    req = requests.get('https://ventox.lol')
    print(req.status_code)