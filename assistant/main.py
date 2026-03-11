from colorama import init
from assistant.commands import commands_resolver
from assistant.storage import load_data, save_data
from assistant.utils import console, print_help_table, HELP_INFO

def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        return "", []

    cmd, *args = parts
    cmd = cmd.strip().lower()

    return cmd, [arg.strip() for arg in args]


def main():
    init(autoreset=True, strip=False, convert=False)
    contacts, notes = load_data()
    console("Welcome to AmigoNotesBot!")
    try:
        while True:
            try:
                user_input = input("Enter a command: ")
            except KeyboardInterrupt:
                console("👋  Good bye!")
                break

            command, args = parse_input(user_input)

            if command in ["close", "exit"]:
                console("👋  Good bye!")
                break

            if command in ["hello", "hi"]:
                console("How can I help you?")
                continue

            if command == "help":
                print_help_table(HELP_INFO)
                continue

            command_data = commands_resolver.COMMANDS.get(command)

            if not command_data:
                console("Invalid command.", "error")
                continue

            handler = command_data["handler"]
            entity = contacts if command_data["entity_type"] == "contacts" else notes

            result = handler(args, entity)

            if result:
                console(result, "success")
    except Exception as e:
        console(e, "error")
    finally:
        save_data(contacts, notes)
