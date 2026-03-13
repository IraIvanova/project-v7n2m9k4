from assistant.errors import ContactNotFoundError


def get_contact_or_raise(book, name):
    record = book.find(name)
    if record is None:
        raise ContactNotFoundError("Contact not found.")
    return record