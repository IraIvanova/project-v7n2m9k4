import re
from datetime import datetime
from assistant.errors.exceptions import (
    InvalidNameError,
    InvalidPhoneError,
    InvalidEmailError,
    AddressBookError,
)


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if not value.strip():
            raise InvalidNameError("Name can't be empty.")
        super().__init__(value.strip())


class Phone(Field):
    def __init__(self, value):
        digits = re.sub(r'\D', '', value)
        if not self.validate(digits):
            raise InvalidPhoneError("Phone must contain exactly 10 digits.")
        super().__init__(digits)

    @staticmethod
    def validate(value):
        return len(value) == 10


class Email(Field):
    def __init__(self, value):
        if not self.validate(value):
            raise InvalidEmailError("Invalid email format.")
        super().__init__(value)

    @staticmethod
    def validate(value):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, value) is not None


class Address(Field):
    pass


class Birthday(Field):
    def __init__(self, value):
        try:
            date = datetime.strptime(value, "%d.%m.%Y")
            super().__init__(date)
        except ValueError:
            raise AddressBookError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")
