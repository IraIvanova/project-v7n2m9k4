from assistant.errors.errors_handler import input_error
from assistant.errors.exceptions import ContactNotFoundError


@input_error
def add_email(args, book):
    name, email = args
    record = book.find(name)
    if record is None:
        raise ContactNotFoundError("Contact not found.")
    record.add_email(email)
    return "Email added."


@input_error
def edit_email(args, book):
    name, email = args
    record = book.find(name)
    if record is None:
        raise ContactNotFoundError("Contact not found.")
    record.edit_email(email)
    return "Email updated."


@input_error
def remove_email(args, book):
    name = args[0]
    record = book.find(name)
    if record is None:
        raise ContactNotFoundError("Contact not found.")
    record.delete_email()
    return "Email deleted."


@input_error
def show_email(args, book):
    name = args[0]
    record = book.find(name)
    if record is None:
        raise ContactNotFoundError("Contact not found.")
    if record.email is None:
        return "Email not set."
    return str(record.email)
