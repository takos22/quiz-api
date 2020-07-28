import requests

URL = "http://127.0.0.1:5000"

# Random question
r = requests.get(URL + "/question")
print(r.json())

# Answer to that question
r = requests.get(URL + f"/answer/{r.json()['id']}")
print(r.json())

# Random question from the "Tech" category
r = requests.get(URL + "/question/1")
print(r.json())

# Answer to that question
r = requests.get(URL + f"/answer/{r.json()['id']}")
print(r.json())

# 404 error because there's no category 0
r = requests.get(URL + "/question/0")
print(r.status_code)
print(r.json())

# 404 error because there's no question 0
r = requests.get(URL + "/answer/0")
print(r.status_code)
print(r.json())
