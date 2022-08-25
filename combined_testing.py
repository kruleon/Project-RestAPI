import requests
import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# enter ANY user_name and user_id vars to POST for testing:
user_name = "test2"
user_id = 2


try:
    # 1. POST any user data (vars above)
    res_post = requests.post(f'http://127.0.0.1:5000/users/{user_id}', json={"user_name": f'{user_name}'})
    if res_post.ok:
        print("SUCCESS: POST:", res_post.json(), "code:", res_post.status_code)
    else:
        print("ERROR: POST failed:", res_post.json(), "code:", res_post.status_code)
        raise Exception("POST", "test failed")


    # 2 - GET request for the above user data
    res_get = requests.get(f'http://127.0.0.1:5000/users/{user_id}')

    # Submit a GET request to make sure status code is 200 and data equals to the posted data.
    if res_get.ok:
        res_payload = res_get.json()
        user_name_get = res_payload['user_name']


        # 3 - query db for user_name per user_id
        conn = pymysql.connect(host='remotemysql.com', port=3306, user='bywqDlIBKA', passwd='ZXBMcpqgxv',
                               db='bywqDlIBKA')
        # conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_leondb', passwd='gysc6K3?vxcA2Pk',
        #                    db='freedb_leondb')
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
            raise Exception("DB", "test failed")

    else:
        print("\n >> ERROR: GET: response failed", res_get.json(), "code:", res_get.status_code, ">>")
        raise Exception("GET", "test failed")


# Start a Selenium Webdriver session.
    driver = webdriver.Chrome(executable_path="C:\\Users\\leon\\Desktop\\chromedriver_win32\\chromedriver.exe")

# Navigate to web interface URL using the new user id.
    driver.get(f'http://127.0.0.1:5001/users/get_user_data/{user_id}')
    try:
        if driver.find_element_by_id("user").is_displayed():
            print(driver.find_element_by_id("user").text)
    except NoSuchElementException:
        print("user - no such element exception")

    try:
        if driver.find_element_by_id("error").is_displayed():
            print(driver.find_element_by_id("error").text)
            raise Exception("Web Element", "test failed")
    except NoSuchElementException as e:
        print("error - no such element exception")

except Exception as e:
    print(e, "test failed")
