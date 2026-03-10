class AddressBookError(Exception):
    pass


class InvalidPhoneError(AddressBookError):
    pass


class InvalidEmailError(AddressBookError):
    pass


class InvalidNameError(AddressBookError):
    pass


class ContactNotFoundError(AddressBookError):
    pass


class FieldNotSetError(AddressBookError):
    pass
