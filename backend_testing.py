import requests
import pymysql


# change the following USER_NAME and USER_ID vars to input for testing:
user_name = "john"
user_id = 1


# 1 - POST with above user data vars
res_post = requests.post(f'http://127.0.0.1:5000/users/{user_id}', json={"user_name": f'{user_name}'})
if res_post.ok:
    print("SUCCESS: POST:", res_post.json(), "code:", res_post.status_code)
else:
    print("ERROR: POST failed:", res_post.json(), "code:", res_post.status_code)


# 2 - GET request for the above user data
res_get = requests.get(f'http://127.0.0.1:5000/users/{user_id}')

# Submit a GET request to make sure status code is 200 and data equals to the posted data.
if res_get.ok:
    res_payload = res_get.json()
    user_name_get = res_payload['user_name']

# 3 - query db for user_name per user_id
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='bywqDlIBKA', passwd='ZXBMcpqgxv', db='bywqDlIBKA')
    # conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_leondb', passwd='gysc6K3?vxcA2Pk',
    #                        db='freedb_leondb')
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute("SELECT user_name FROM users WHERE user_id = %s", user_id)


# Confirm posted data was stored inside DB (users table).
    user_name_db = ""
    for user_name_list in cursor:
        user_name_db = user_name_list[0]

    cursor.close()
    conn.close()

    if user_name_get == user_name_db == user_name:
        print("SUCCESS: GET:", res_get.json(), "code:", res_get.status_code)
        print("\nGET requested user name:", user_name_get)
        print("DB requested user name:", user_name_db)
        print("\n>> COMPLETED SUCCESSFULLY: backend_testing: user data equals to the posted data and successfully stored in DB (users table) << ")

    else:
        print("\n >> ERROR: posted data not confirmed << ")
        print("GET response json", res_get.json(), "code:", res_get.status_code)
        print("\nGET requested user name:", user_name_get)
        print("DB requested user name:", user_name_db)

else:
    print("\n >> ERROR: GET: response failed", res_get.json(), "code:", res_get.status_code, ">>")



