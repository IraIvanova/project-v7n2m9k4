from assistant.errors.errors_handler import input_error
from assistant.utils.contact_utils import get_contact_or_raise


@input_error
def add_birthday(args, book):
    name, birthday = args
    record = get_contact_or_raise(book, name)
    record.add_birthday(birthday)
    return "Birthday added."


@input_error
def edit_birthday(args, book):
    name, birthday = args
    record = get_contact_or_raise(book, name)
    record.add_birthday(birthday)
    return "Birthday updated."


@input_error
def remove_birthday(args, book):
    name = args[0]
    record = get_contact_or_raise(book, name)
    record.birthday = None
    return "Birthday deleted."


@input_error
def show_birthday(args, book):
    name = args[0]
    record = get_contact_or_raise(book, name)
    if record.birthday is None:
        return "Birthday not set."
    return str(record.birthday)


def get_upcoming_birthdays(_args, book):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays."
    return "\n".join(f"{item['name']} - {item['congratulation_date']}" for item in upcoming)
