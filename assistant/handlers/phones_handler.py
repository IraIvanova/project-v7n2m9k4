from assistant.errors.errors_handler import input_error
from assistant.errors.exceptions import ContactNotFoundError
from assistant.validators import validate_args


@input_error
def add_phone(args, book):
    validate_args(args, 2, "Please provide name and phone.")
    name, phone = args[0], args[1]
    record = book.find(name)
    if record is None:
        raise ContactNotFoundError("Contact not found.")
    book.is_phone_unique(phone)
    record.add_phone(phone)
    return "Phone added."


@input_error
def edit_phone(args, book):
    validate_args(args, 3, "Please provide name, old phone, and new phone.")
    name, old_phone, new_phone = args[0], args[1], args[2]
    record = book.find(name)
    if record is None:
        raise ContactNotFoundError("Contact not found.")
    book.is_phone_unique(new_phone)
    record.edit_phone(old_phone, new_phone)
    return "Phone updated."


@input_error
def remove_phone(args, book):
    validate_args(args, 2, "Please provide name and phone.")
    name, phone = args[0], args[1]
    record = book.find(name)
    if record is None:
        raise ContactNotFoundError("Contact not found.")
    record.remove_phone(phone)
    return "Phone deleted."


@input_error
def show_phones(args, book):
    validate_args(args, 1, "Please provide name.")
    name = args[0]
    record = book.find(name)
    if record is None:
        raise ContactNotFoundError("Contact not found.")
    if not record.phones:
        return "No phones set."
    return ", ".join(str(p) for p in record.phones)
