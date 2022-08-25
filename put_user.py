import requests

res = requests.put('http://127.0.0.1:5000/users/1', json={'user_name': 'george'})

print(res.json(), "code:", res.status_code)
print(res)


# requests.exceptions.ConnectionError: ('Connection aborted.', ConnectionResetError(10054,
# 'An existing connection was forcibly closed by the remote host', None, 10054, None))