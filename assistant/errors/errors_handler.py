from functools import wraps
from assistant.utils import console
from assistant.errors.exceptions import AddressBookError

def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except ValueError as e:
            console(str(e), "error")

        except AddressBookError as e:
            console(str(e), "error")

        except IndexError:
            console("Enter required arguments.", "error")

        except KeyError:
            console("Contact not found.", "error")

        except Exception as e:
            console(f"Unexpected error: {e}", "error")

    return wrapper