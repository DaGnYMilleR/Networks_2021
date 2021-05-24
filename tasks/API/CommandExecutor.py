class CommandExecutor:
    def __init__(self):
        self.commands = []

    def register_command(self, command):
        self.commands.append(command)

    def execute(self, args):
        if len(args[0]) == 0:
            print("Please specify <command> as the first command line argument")
            return
        command_name = args[0]
        cmd = self.find_command(command_name)
        if len(cmd) == 0:
            print(f"Sorry. unknown command {command_name}")
            return
        cmd[0].execute(args[1::])

    def find_command(self, name):
        return [x for x in self.commands if x.name == name]