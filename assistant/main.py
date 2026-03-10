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

            handler, entity_type = commands_resolver.COMMANDS[command]
            entity = contacts if entity_type == "contacts" else notes

            if handler:
                handler(*args, entity)
            else:
                print("Invalid command.", "error")
                continue

    except Exception as e:
        print(e)
    finally:
        save_data()
