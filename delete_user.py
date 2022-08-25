import requests

res = requests.delete('http://127.0.0.1:5000/users/37')

print(res.json(), "code:", res.status_code)
print(res)
