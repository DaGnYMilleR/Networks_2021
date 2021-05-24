import ssl
import socket
import base64

def request(socket, request):
    socket.send((request + '\n').encode())
    recv_data = socket.recv(65535)
    return recv_data


host_addr = "api.github.com"#'webdav.yandex.ru'
port = 443
login = "c2Ftb3NoY2tpbmFydGVtQHlhbmRleC5ydTpuNDMyYlljUw=="
unique_yandex_password = "c2Ftb3NoY2tpbmFydGVtQHlhbmRleC5ydTppZGJyZHlqemJicGVrc2xk"


def create_request_get(password, filename):
    print(123)
    return f"""
GET /users/lapakota/repos HTTP/1.1\r
Host: api.github.com\r
user-agent: 'python'
username: "lapakota"\r
"""


def delete_request(password, filename):
    return f"""
DELETE /{filename} HTTP/1.1
Host: webdav.yandex.ru
Accept: */*
Authorization: Basic {password}
"""


login_base64 = "c2Ftb3NoY2tpbmFydGVtQHlhbmRleC5ydQ=="
password_base64 = "bjQzMmJZY1M="


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((host_addr, port))
    client = ssl.wrap_socket(client)
    a = request(client, create_request_get(unique_yandex_password, "test.txt"))
    print(a.decode())
