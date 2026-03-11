from assistant.errors.errors_handler import input_error
from assistant.utils.contact_utils import get_contact_or_raise


@input_error
def add_email(args, book):
    name, email = args
    record = get_contact_or_raise(book, name)
    record.add_email(email)
    return "Email added."


@input_error
def edit_email(args, book):
    name, email = args
    record = get_contact_or_raise(book, name)
    record.edit_email(email)
    return "Email updated."


@input_error
def remove_email(args, book):
    name = args[0]
    record = get_contact_or_raise(book, name)
    record.delete_email()
    return "Email deleted."


@input_error
def show_email(args, book):
    name = args[0]
    record = get_contact_or_raise(book, name)
    if record.email is None:
        return "Email not set."
    return str(record.email)
