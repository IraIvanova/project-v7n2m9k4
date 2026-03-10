from assistant.commands import commands_resolver
from assistant.storage.storage import load_data, save_data

def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        return "", []

    cmd, *args = parts
    cmd = cmd.strip().lower()

    return cmd, *[arg.strip() for arg in args]

def main():
    contacts, notes = load_data()
    print("Welcome to AmigoNotesBot!")

    try:
        while True:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("👋  Good bye!")
                break

            if command in ["hello", "hi"]:
                print("How can I help you?")
                continue

            command_data = commands_resolver.COMMANDS.get("command")

            if not command_data:
                print("Invalid command.")
                continue

            handler = command_data["handler"]
            entity = contacts if command_data["entity_type"] == "contacts" else notes

            handler(args, entity)
    except Exception as e:
        print(e)
    finally:
        save_data()
