import requests

URL = "http://127.0.0.1:5000"

r = requests.get(URL + "/question")
print(r.json())

r = requests.get(URL + f"/answer/{r.json()['id']}")
print(r.json())

r = requests.get(URL + "/question/1")
print(r.json())

r = requests.get(URL + f"/answer/{r.json()['id']}")
print(r.json())

r = requests.get(URL + "/question/4")
print(r.status_code)
print(r.json())

r = requests.get(URL + "/answer/5")
print(r.status_code)
print(r.json())
