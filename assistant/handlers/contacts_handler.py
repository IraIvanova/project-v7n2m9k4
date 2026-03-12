from assistant.errors.errors_handler import input_error
from assistant.errors.exceptions import ContactNotFoundError
from assistant.models.address_book import Record
from assistant.utils.print_contacts_table import print_contacts_table
from assistant.validators import validate_args


@input_error
def add_contact(args, book):
    validate_args(args, 2, "Please provide name and phone.")
    name, phone = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    record.add_phone(phone)
    return message


@input_error
def edit_contact(args, book):
    validate_args(args, 3, "Please provide name, old phone, new phone.")
    name, old_phone, new_phone = args
    record = book.find(name)
    if record is None:
        raise ContactNotFoundError("Contact not found.")
    record.edit_phone(old_phone, new_phone)
    return "Phone updated."


@input_error
def remove_contact(args, book):
    validate_args(args, 1, "Please provide name.")
    name = args[0]
    if book.find(name) is None:
        raise ContactNotFoundError("Contact not found.")
    book.delete(name)
    return "Contact deleted."


@input_error
def show_contact(args, book):
    validate_args(args, 1, "Please provide name.")
    name = args[0]
    record = book.find(name)
    if record is None:
        raise ContactNotFoundError("Contact not found.")
    print_contacts_table([record])


@input_error
def search_contacts(args, book):
    validate_args(args, 2, "Please provide field (name/phone/email/birthday/address) and query.")
    field, query = args[0].lower(), args[1].lower()

    results = []
    for record in book.data.values():
        if field == "name":
            if record.name.value.lower().startswith(query):
                results.append(record)
        elif field == "phone":
            if any(p.value.startswith(query) for p in record.phones):
                results.append(record)
        elif field == "email":
            if record.email and str(record.email).lower().startswith(query):
                results.append(record)
        elif field == "birthday":
            if record.birthday and str(record.birthday).startswith(query):
                results.append(record)
        elif field == "address":
            if record.address and query in str(record.address).lower():
                results.append(record)
        else:
            return "Invalid field. Use: name/phone/email/birthday/address"

    if not results:
        return "No contacts found."
    print_contacts_table(results)


def get_all_contacts(_args, book):
    if not book.data:
        return "Address book is empty."
    print_contacts_table(book.data.values())
