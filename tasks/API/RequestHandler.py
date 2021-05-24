import socket
import ssl


class RequestHandler:
    def __init__(self):
        self.host = "api.github.com"
        self.port = 443

    def send_request_and_get_result(self, request):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((self.host, self.port))
            client = ssl.wrap_socket(client)
            client.settimeout(1)
            client.send((request + '\n').encode())
            res = ""
            while True:
                try:
                    recv_data = client.recv(65536)
                    if not recv_data:
                        break
                    res += recv_data.decode()
                except socket.timeout:
                    break
            return res