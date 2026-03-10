from assistant.errors.exceptions import AddressBookError


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except AddressBookError as e:
            return str(e)

        except IndexError:
            return "Enter required arguments."

        except KeyError:
            return "Contact not found."

    return wrapper