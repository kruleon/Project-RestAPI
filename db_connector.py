import pymysql


# # # getting current date time - no microseconds
def current_date():
    from datetime import datetime
    creation_date = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    return creation_date


# # # Establishing a connection to DB
def connect_db():
    #import pymysql
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='bywqDlIBKA', passwd='ZXBMcpqgxv', db='bywqDlIBKA')
    # conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_leondb', passwd='gysc6K3?vxcA2Pk',
    #                        db='freedb_leondb')
    conn.autocommit(True)
    my_cursor = conn.cursor()
    return my_cursor


# # # Reading\Getting all data from table
def get_all_data_db():
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='bywqDlIBKA', passwd='ZXBMcpqgxv', db='bywqDlIBKA')

    # conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_leondb', passwd='gysc6K3?vxcA2Pk',
    #                        db='freedb_leondb')
    conn.autocommit(True)
    cursor = conn.cursor()
    # cursor.execute("SELECT * FROM bywqDlIBKA.users;")
    cursor.execute("SELECT * FROM freedb_leondb.users")
    for row in cursor:
        print(row)
    cursor.close()
    conn.close()


# # get user_name via given user_id from table
def get_user_name_from_db(user_id):
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='bywqDlIBKA', passwd='ZXBMcpqgxv', db='bywqDlIBKA')
    # conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_leondb', passwd='gysc6K3?vxcA2Pk',
    #                        db='freedb_leondb')
    conn.autocommit(True)
    cursor = conn.cursor()
    # cursor = connect_db()
    cursor.execute("SELECT user_name FROM users WHERE user_id = %s", user_id)
    for user_name_list in cursor:
        print("user name", user_name_list[0], ", user id", user_id)
        cursor.close()
        conn.close()
        return user_name_list[0]


# # get every user_name for given user_id from Table
def user_name_via_user_id_select(user_name):
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='bywqDlIBKA', passwd='ZXBMcpqgxv', db='bywqDlIBKA')
    # conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_leondb', passwd='gysc6K3?vxcA2Pk',
    #                        db='freedb_leondb')
    conn.autocommit(True)
    cursor = conn.cursor()
    user_id_list = []
    cursor.execute("SELECT user_id FROM users WHERE user_name = %s", user_name)
    for row in cursor:
        for uid in row:
            user_id_list.append(uid)
    print(user_id_list)
    print(user_id_list[0])
    cursor.close()
    conn.close()
    return user_id_list[0]


# # convert_user_id_column_to_user_id_list
def get_user_id_list_db():
    string_list = []
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='bywqDlIBKA', passwd='ZXBMcpqgxv', db='bywqDlIBKA')
    # conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_leondb', passwd='gysc6K3?vxcA2Pk',
    #                        db='freedb_leondb')
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users")
    user_id_column = cursor
    for row in user_id_column:
        for char in row:
            string_list.append(char)
    cursor.close()
    conn.close()
    return string_list


def id_exist(user_id):
    user_id_list = get_user_id_list_db()
    for uid in user_id_list:
        if uid == int(user_id):
            # print("user id", user_id, "exists")
            return True


# # # Writing\Inserting data into table
def insert_data_db(user_id, user_name, creation_date):
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='bywqDlIBKA', passwd='ZXBMcpqgxv', db='bywqDlIBKA')
    # conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_leondb', passwd='gysc6K3?vxcA2Pk',
    #                        db='freedb_leondb')
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (user_id, user_name, creation_date) VALUES (%s, %s, %s)", (user_id, user_name, creation_date))
    print(f"new user_id {user_id} inserted to users Table. user id list updated:", get_user_id_list_db())
    cursor.close()
    conn.close()


# # # Updating data into table
def update_user_db(user_id, user_name):
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='bywqDlIBKA', passwd='ZXBMcpqgxv', db='bywqDlIBKA')
    # conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_leondb', passwd='gysc6K3?vxcA2Pk',
    #                        db='freedb_leondb')
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET user_name=%s WHERE user_id=%s", (user_name, user_id))
    cursor.close()
    conn.close()


# # Deleting all data from table
def delete_data_db():
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='bywqDlIBKA', passwd='ZXBMcpqgxv', db='bywqDlIBKA')
    # conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_leondb', passwd='gysc6K3?vxcA2Pk',
    #                        db='freedb_leondb')
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users")
    cursor.close()
    conn.close()
    print("all data deleted")


# # Delete user data via user_id
def delete_user_db(user_id):
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='bywqDlIBKA', passwd='ZXBMcpqgxv', db='bywqDlIBKA')
    # conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_leondb', passwd='gysc6K3?vxcA2Pk',
    #                        db='freedb_leondb')
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE user_id=%s", user_id)
    cursor.close()
    conn.close()


def close_connect_db():
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='bywqDlIBKA', passwd='ZXBMcpqgxv', db='bywqDlIBKA')
    # conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_leondb', passwd='gysc6K3?vxcA2Pk', db='freedb_leondb')
    cursor = conn.cursor()
    cursor.close()
    conn.close()


# if __name__ == "__main__":
#     print("\ndb_connector executed directly\n")
#     # get_all_data_db()
#     # insert_data_db(5, 'leon', current_date())
#     # delete_data_db()
#     # close_connect_db()
# elif __name__ == "__rest_api__":
#     print("\ndb_connector executed via rest_app\n")
#     # close_connect_db()

# else:
#     print("\ndb_connector executed via web_app\n")


