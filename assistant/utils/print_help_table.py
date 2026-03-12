from .console import console
from tabulate import tabulate

HELP_INFO = {
    "CONTACT": [
        {"command": "add-contact", "args": "<name> <phone>"},
        {"command": "delete-contact", "args": "<name>"},
        {"command": "show-contact", "args": "<name>"},
        {"command": "all-contacts", "args": "-"},
        {"command": "contacts-birthdays", "args": "-"},
        {"command": "search-contacts", "args": "<field> <query>"},
    ],

    "FIELDS": [
        {"command": "add-address", "args": "<name> <address>"},
        {"command": "edit-address", "args": "<name> <new address>"},
        {"command": "delete-address", "args": "<name>"},
        {"command": "show-address", "args": "<name>"},
        {"command": "add-email", "args": "<name> <email>"},
        {"command": "edit-email", "args": "<name> <email>"},
        {"command": "delete-email", "args": "<name>"},
        {"command": "show-email", "args": "<name>"},
        {"command": "add-birthday", "args": "<name> <birthday>"},
        {"command": "edit-birthday", "args": "<name> <birthday>"},
        {"command": "delete-birthday", "args": "<name>"},
        {"command": "show-birthday", "args": "<name>"},
        {"command": "add-phone", "args": "<name> <phone>"},
        {"command": "edit-phone", "args": "<name> <old_phone> <new_phone>"},
        {"command": "delete-phone", "args": "<name>"},
        {"command": "show-phone", "args": "<name>"},
    ],

    "NOTES": [
        {"command": "add-note", "args": "<text> <#tag1> <#tag2> ..."},
        {"command": "edit-note", "args": "<id> <new text> <#tag1> <#tag2> ..."},
        {"command": "delete-note", "args": "<id>"},
        {"command": "delete-tag", "args": "<id> <#tag>"},
        {"command": "search-notes", "args": "<field> <query>"},
        {"command": "sort-notes", "args": "<field> <query>"},
        {"command": "all-notes", "args": "-"},
    ],

    "SYSTEM": [
        {"command": "hello", "args": "-"},
        {"command": "hi", "args": "-"},
        {"command": "help", "args": "-"},
        {"command": "exit", "args": "-"},
        {"command": "close", "args": "-"},
    ],
}


def print_help_table(commands):

    categories = {
        "CONTACT": [],
        "FIELDS": [],
        "NOTES": [],
        "SYSTEM": []
    }

    for category, items in commands.items():
        for cmd in items:
            categories[category].append([
                cmd["command"],
                cmd["args"]
            ])

    tables = []

    for category in ["CONTACT", "FIELDS", "NOTES", "SYSTEM"]:
        tables.append(
            tabulate(
                categories[category],
                headers=["Command", "Arguments"],
                tablefmt="simple"
            )
        )

    console(
        tabulate(
            [tables],
            headers=["CONTACTS COMMANDS", "FIELDS COMMANDS", "NOTES COMMANDS", "SYSTEM COMMANDS"],
            tablefmt="fancy_grid"
        )
    )