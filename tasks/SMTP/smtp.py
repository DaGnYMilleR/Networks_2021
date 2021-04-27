import base64
import socket
import ssl


def request(socket, request):
    socket.send((request + '\n').encode())
    recv_data = socket.recv(65535).decode()
    return recv_data


host_addr = 'smtp.yandex.ru'
port = 465
user_name = 'samoshckinartem'
password ='n432bYcS'
recipient_name = 'hard-sign-meme'


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((host_addr, port))
    client = ssl.wrap_socket(client)
    print(client.recv(1024))
    print(request(client, 'EHLO samoshckinartem'))
    base64login = base64.b64encode(user_name.encode()).decode()

    base64password = base64.b64encode(password.encode()).decode()
    print(request(client, 'AUTH LOGIN'))
    print(request(client, base64login))
    print(request(client, base64password))
    print(request(client, f"MAIL FROM:{user_name}@ya.ru"))
    print(request(client, f"RCPT TO:{recipient_name}@ya.ru"))
    print(request(client, 'DATA'))
    with open('msg.txt') as file:
        print(request(client, ''.join(file.readlines())))


