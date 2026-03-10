from colorama import init
from assistant.commands import commands_resolver
from assistant.storage import load_data, save_data
from assistant.utils import console

def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        return "", []

    cmd, *args = parts
    cmd = cmd.strip().lower()

    return cmd, *[arg.strip() for arg in args]

def main():
    init(autoreset=True, strip=False, convert=False)
    load_data()
    console("Welcome to AmigoNotesBot!")

    try:
        while True:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                console("👋  Good bye!")
                break

            if command in ["hello", "hi"]:
                console("How can I help you?")
                continue

            handler = commands_resolver.COMMANDS.get(command)

            if handler:
                handler(*args)
            else:
                console("Invalid command.", "error")
                continue

    except Exception as e:
        console(e, "error")
    finally:
        save_data()
