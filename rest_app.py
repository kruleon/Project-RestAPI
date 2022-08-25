from flask import Flask, request
app = Flask(__name__)


# getting current date time - no microseconds
def current_date():
    from datetime import datetime
    creation_date = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    # print(creation_date)
    return creation_date


# local users' storage (new empty dictionary)
users = {}


@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user_get(user_id):
    from db_connector import get_user_name_from_db, id_exist
    if request.method == 'GET':
        try:
            if id_exist(user_id):
                user_name = get_user_name_from_db(user_id)
                return {'status': 'ok', 'user_id': user_id, 'user_name': user_name}, 200
        except ValueError as value_error:
            print(value_error, "\nuser_id wrong value, enter number instead")
        try:
            return {'status': 'error', 'reason': "no such id"}, 500
        except TypeError as type_error:
            print(type_error)

    elif request.method == 'POST':
        from db_connector import insert_data_db, id_exist
        request_data = request.json
        user_name = request_data.get('user_name')
        users[user_id] = user_name
        if id_exist(user_id):
            return {'status': 'error', 'reason': "id already exists"}, 500
        insert_data_db(user_id, user_name, current_date())
        return {'status': 'ok', 'user added': user_name}, 200

    elif request.method == 'PUT':
        from db_connector import id_exist, update_user_db
        request_data = request.json
        user_name = request_data.get('user_name')
        if id_exist(user_id):
            print(f"id {user_id} - user name updated to:", user_name)
            update_user_db(user_id, user_name)
            return {'status': 'ok', 'user_updated': user_name}, 200
        return {'status': 'error', 'reason': "no such id"}, 500

    elif request.method == 'DELETE':
        from db_connector import id_exist, delete_user_db
        if id_exist(user_id):
            delete_user_db(user_id)
            return {'status': 'ok', 'user_id_deleted': user_id}, 200
        return {'status': 'error', 'reason': "no such id"}, 500


# # automatic termination
import os
import signal


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'rest_app Server stopped'


app.run(host='127.0.0.1', debug=True, port=5000)
