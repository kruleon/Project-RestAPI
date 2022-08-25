import requests
from requests.exceptions import ChunkedEncodingError
from urllib3.exceptions import NewConnectionError, MaxRetryError, ProtocolError

# try:

res_5000 = requests.get('http://127.0.0.1:5000/stop_server')
print(res_5000.text)
res_5001 = requests.get('http://127.0.0.1:5001/stop_server')
print(res_5001.text)


# except (ConnectionRefusedError, NewConnectionError, MaxRetryError, ConnectionResetError, ProtocolError, ChunkedEncodingError):
#     print("try - No connection could be made because the target machine actively refused it")
