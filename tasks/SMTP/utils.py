import base64


def get_file_content(filename):
    with open(filename, "rb") as f:
        image_str = f.read()
        return base64.b64encode(image_str).decode()


def get_base64string(msg):
    return base64.b64encode(msg.encode()).decode()
