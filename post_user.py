import requests

res = requests.post('http://127.0.0.1:5000/users/20', json={'user_name': 'dror'})

print(res.json(), "code:", res.status_code)
print(res)
