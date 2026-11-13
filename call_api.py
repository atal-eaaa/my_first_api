import requests as re

url = "http://127.0.0.1:8000/calculate_score"
body = [1,2,2,2,3]

r = re.post(url, json = body, timeout = 5)

print(r.status_code, r.json())



