class Text:
    def __init__(self, filename: str):
        with open(filename, "r", encoding="utf8") as f:
            message = "".join(f.readlines())
        self.content = ""
        self.content += f"Content-Transfer-Encoding: 8bit\n"
        self.content += f"Content-Type: text/plain; charset=utf-8\n\n"
        self.content += message.replace("\n.", "\n..")
