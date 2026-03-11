from assistant.errors.errors_handler import input_error
from assistant.errors.exceptions import ContactNotFoundError
from assistant.models.address_book import Record
from assistant.utils.contact_utils import get_contact_or_raise

def _set_favorite_status(book, name, is_favorite):
    record = get_contact_or_raise(book, name)
    record.is_favorite = is_favorite
    return record

@input_error
def add_contact(args, book):
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
    name, old_phone, new_phone = args
    record = get_contact_or_raise(book, args[0])
    record.edit_phone(old_phone, new_phone)
    return "Phone updated."


@input_error
def remove_contact(args, book):
    name = args[0]
    if book.find(name) is None:
        raise ContactNotFoundError("Contact not found.")
    book.delete(name)
    return "Contact deleted."


@input_error
def show_contact(args, book):
    record = get_contact_or_raise(book, args[0])
    return "; ".join(p.value for p in record.phones)


def search_contacts(args, book):
    query = args[0].lower() if args else ""
    results = [str(r) for r in book.data.values() if query in r.name.value.lower()]
    return "\n".join(results) if results else "No contacts found."


def get_all_contacts(_args, book, favorite=False):
    if not book.data:
        return "Address book is empty."
    return "\n".join(str(record) for record in book.data.values())

@input_error
def mark_favorite(args, book):
    _set_favorite_status(book, args[0], True)
    return "Contact marked as favorite."

@input_error
def unmark_favorite(args, book):
    _set_favorite_status(book, args[0], False)
    return "Contact unmarked as favorite."

def get_favorite_contacts(_args, book):
    favorites = [str(record) for record in book.data.values() if record.is_favorite]
    if not favorites:
        return "No favorite contacts yet."
    return "\n".join(favorites)


