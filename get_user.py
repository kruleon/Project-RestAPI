import requests

res = requests.get('http://127.0.0.1:5000/users/1')

print(res.json(), "code:", res.status_code)
print(res)


# res = requests.get('http://127.0.0.1:5001/users/get_user_data/13')
#
# # print(res.json(), "code:", res.status_code)
# print(res)
