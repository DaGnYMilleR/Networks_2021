class PingCommand:
    def __init__(self):
        self.name = "ping"

    def execute(self, args):
        print("pong")