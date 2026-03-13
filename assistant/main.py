from colorama import init
from assistant.commands import commands_resolver
from assistant.storage import load_data, save_data
from assistant.utils import console, print_help_table, HELP_INFO
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from thefuzz import process

def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        return "", []

    cmd, *args = parts
    cmd = cmd.strip().lower()

    return cmd, [arg.strip() for arg in args]

def suggest_command(user_input, commands):
    """Пошук найбільш схожої команди за алгоритмом Левенштейна."""
    if not user_input:
        return None
    # Отримуємо найкращий збіг з порогом схожості (наприклад, 60%)
    match, score = process.extractOne(user_input, commands)
    return match if score >= 60 else None

def main():
    init(autoreset=True, strip=False, convert=False)
    contacts, notes = load_data()
    
    # Список всіх доступних команд для автодоповнення та пошуку
    available_commands = list(commands_resolver.COMMANDS.keys()) + \
                         ["close", "exit", "hello", "hi", "help"]
    
    # Налаштування автодоповнювача (Tab)
    completer = WordCompleter(available_commands, ignore_case=True, match_middle=False, sentence=True)
    session = PromptSession(completer=completer)

    console("Welcome to AmigoNotesBot!")
    try:
        while True:
            try:
                # Використання prompt_toolkit замість input()
                user_input = session.prompt("Enter a command: ").strip()
            except (KeyboardInterrupt, EOFError):
                console("👋  Good bye!")
                break

            if not user_input:
                continue

            command, args = parse_input(user_input)

            # Перевірка наявності команди
            if command not in available_commands:
                suggestion = suggest_command(command, available_commands)
                if suggestion:
                    console(f"Invalid command. Did you mean '{suggestion}'?", "warning")
                else:
                    console("Invalid command. Type 'help' to see available commands.", "error")
                continue

            # Обробка системних команд
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
