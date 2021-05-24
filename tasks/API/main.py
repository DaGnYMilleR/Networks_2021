from API.commands.PingCommand import PingCommand
from API.commands.RepositoryInfoCommand import RepositoryInfoCommand
from API.CommandExecutor import CommandExecutor


def register_commands(command_executor):
    command_executor.register_command(PingCommand())
    command_executor.register_command(RepositoryInfoCommand())


def main():
    executor = CommandExecutor()
    register_commands(executor)
    while True:
        print("> ", end="")
        line = input()
        if not line or line == "exit":
            return
        executor.execute(line.split())


if __name__ == '__main__':
    main()
