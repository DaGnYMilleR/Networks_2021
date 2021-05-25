import time
import utils


class Content:
    def __init__(self, user, targets, subject):
        targets_addr = ",".join(f"\"{x}\" <{x}>" for x in targets)
        self.boundary = "kdsljflsdkjf" + str(time.time()) + "lkdsjflsdkjfldskj"
        self.header = ""
        self.header += f"From:{user}\n"
        self.header += f"To:{targets_addr}\n"
        self.header += f"Subject: =?UTF-8?B?{utils.get_base64string(subject)}?=\n"
        self.header += f"Content-type: multipart/mixed; boundary={self.boundary}\n\n"
        self.message = ""

    def append(self, message):
        self.message += self.start_boundary() + "\n" + message

    def end(self):
        self.message += "\n" + self.end_boundary() + "\n.\n"

    def start_boundary(self):
        return f"--{self.boundary}"

    def end_boundary(self):
        return f"--{self.boundary}--"

    @property
    def content(self):
        return self.header + "\n" + self.message