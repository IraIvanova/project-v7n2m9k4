from assistant.errors.errors_handler import input_error
from assistant.errors.exceptions import AddressBookError
from assistant.validators import validate_args
from assistant.utils.contact_utils import get_contact_or_raise



@input_error
def add_birthday(args, book):
    validate_args(args, 2, "Please provide name and birthday.")
    name, birthday = args
    record = get_contact_or_raise(book, name)
    if record.birthday is not None:
        raise AddressBookError("Birthday already set. Use edit-birthday to change it.")
    record.add_birthday(birthday)
    return "Birthday added."


@input_error
def edit_birthday(args, book):
    validate_args(args, 2, "Please provide name and birthday.")
    name, birthday = args
    record = get_contact_or_raise(book, name)
    record.add_birthday(birthday)
    return "Birthday updated."


@input_error
def remove_birthday(args, book):
    validate_args(args, 1, "Please provide name.")
    record = get_contact_or_raise(book, args[0])
    record.birthday = None
    return "Birthday deleted."


@input_error
def show_birthday(args, book):
    validate_args(args, 1, "Please provide name.")
    record = get_contact_or_raise(book, args[0])
    if record.birthday is None:
        return "Birthday not set."
    return str(record.birthday)


def get_upcoming_birthdays(_args, book):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays."
    return "\n".join(f"{item['name']} - {item['congratulation_date']}" for item in upcoming)
