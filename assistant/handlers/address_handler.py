from assistant.errors.errors_handler import input_error
from assistant.errors.exceptions import ContactNotFoundError


@input_error
def add_address(args, book):
    name, *address = args
    record = book.find(name)
    if record is None:
        raise ContactNotFoundError("Contact not found.")
    record.add_address(" ".join(address))
    return "Address added."


@input_error
def edit_address(args, book):
    name, *address = args
    record = book.find(name)
    if record is None:
        raise ContactNotFoundError("Contact not found.")
    record.edit_address(" ".join(address))
    return "Address updated."


@input_error
def remove_address(args, book):
    name = args[0]
    record = book.find(name)
    if record is None:
        raise ContactNotFoundError("Contact not found.")
    record.delete_address()
    return "Address deleted."


@input_error
def show_address(args, book):
    name = args[0]
    record = book.find(name)
    if record is None:
        raise ContactNotFoundError("Contact not found.")
    if record.address is None:
        return "Address not set."
    return str(record.address)