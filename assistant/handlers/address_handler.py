from assistant.errors.errors_handler import input_error
from assistant.utils.contact_utils import get_contact_or_raise


@input_error
def add_address(args, book):
    name, *address = args
    record = get_contact_or_raise(book, name)
    record.add_address(" ".join(address))
    return "Address added."


@input_error
def edit_address(args, book):
    name, *address = args
    record = get_contact_or_raise(book, name)
    record.edit_address(" ".join(address))
    return "Address updated."


@input_error
def remove_address(args, book):
    name = args[0]
    record = get_contact_or_raise(book, name)
    record.delete_address()
    return "Address deleted."


@input_error
def show_address(args, book):
    name = args[0]
    record = get_contact_or_raise(book, name)
    if record.address is None:
        return "Address not set."
    return str(record.address)