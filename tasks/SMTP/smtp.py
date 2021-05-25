import base64
import socket
import ssl
from content import Content
from text import Text
from config import Config
from attachment import Attachment
import utils


def request(socket, request):
    socket.send((request + '\n').encode())
    recv_data = socket.recv(65535).decode()
    return recv_data


def create_message(message_file, user, targets, subject, attachment_files):
    subject = subject or "No subject"
    content = Content(user, targets, subject)
    msg = Text(message_file)
    if not attachment_files:
        msg.content = f"Subject: =?UTF-8?B?{utils.get_base64string(subject)}?=\n" + msg.content + "\n.\n"
        return msg.content
    attachments = [Attachment(x) for x in attachment_files]
    content.append(msg.content)
    for att in attachments:
        content.append(att.content)
    content.end()
    return content.content


def main():
    config = Config("./config.json")
    message = create_message(config.message_file, config.user_address, config.targets,
                             config.subject, config.attachments)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((config.host_addr, config.port))
        client = ssl.wrap_socket(client)
        print(request(client, f'EHLO {config.user_name}'))
        base64login = base64.b64encode(config.user_address.encode()).decode()
        base64password = base64.b64encode(config.password.encode()).decode()
        print(request(client, 'AUTH LOGIN'))
        print(request(client, base64login))
        print(request(client, base64password))
        err = request(client, f'MAIL FROM:{config.user_address}')
        if err.startswith("503"):
            print("Неверный пароль или логин")
            return
        print(err)
        for target in config.targets:
            print(request(client, f"RCPT TO:{target}"))
        print(request(client, 'DATA'))
        print(request(client, message))


if __name__ == "__main__":
    main()