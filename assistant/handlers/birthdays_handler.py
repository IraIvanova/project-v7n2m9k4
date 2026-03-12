from assistant.errors.errors_handler import input_error
from assistant.errors.exceptions import ContactNotFoundError
from assistant.validators import validate_args


@input_error
def add_birthday(args, book):
    validate_args(args, 2, "Please provide name and birthday.")
    name, birthday = args
    record = book.find(name)
    if record is None:
        raise ContactNotFoundError("Contact not found.")
    record.add_birthday(birthday)
    return "Birthday added."


@input_error
def edit_birthday(args, book):
    validate_args(args, 2, "Please provide name and birthday.")
    name, birthday = args
    record = book.find(name)
    if record is None:
        raise ContactNotFoundError("Contact not found.")
    record.add_birthday(birthday)
    return "Birthday updated."


@input_error
def remove_birthday(args, book):
    validate_args(args, 1, "Please provide name.")
    name = args[0]
    record = book.find(name)
    if record is None:
        raise ContactNotFoundError("Contact not found.")
    record.birthday = None
    return "Birthday deleted."


@input_error
def show_birthday(args, book):
    validate_args(args, 1, "Please provide name.")
    name = args[0]
    record = book.find(name)
    if record is None:
        raise ContactNotFoundError("Contact not found.")
    if record.birthday is None:
        return "Birthday not set."
    return str(record.birthday)


def get_upcoming_birthdays(_args, book):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays."
    return "\n".join(f"{item['name']} - {item['congratulation_date']}" for item in upcoming)
