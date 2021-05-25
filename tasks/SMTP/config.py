import json


class Config:
    def __init__(self, filename: str):
        with open(filename, encoding="utf8") as f:
            conf = json.load(f)
            self.host_addr = conf["host_addr"]
            self.port = conf["port"]
            self.user_address = conf["user_address"]
            self.user_name = conf["user_name"]
            self.password = conf["password"]
            self.targets = conf["targets"]
            self.message_file = conf["message_file"]
            self.subject = conf["subject"]
            self.attachments = conf["attachments"]
