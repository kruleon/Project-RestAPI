from flask import Flask
app = Flask(__name__)


@app.route('/users/get_user_data/<user_id>')
def get_user_name(user_id):
    from db_connector import get_user_name_from_db
    user_name = get_user_name_from_db(user_id)
    if user_name is None:
        return "<H1 id='error'>" "no such user:" + user_id + "</H1>"
    return "<H1 id='user'>" + user_name + "</H1>"


# # automatic termination
import os
import signal


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'web_app Server stopped'


app.run(host='127.0.0.1', debug=True, port=5001)
