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
        normalized = self.normalize(value)
        if not self.validate(normalized):
            raise InvalidPhoneError("Invalid phone number. Use local format 0XXXXXXXXX (10 digits) or international +380XXXXXXXXX / 380XXXXXXXXX (12 digits).")
        super().__init__(normalized)

    @staticmethod
    def normalize(phone: str) -> str:
        digits = re.sub(r'\D', '', phone)
        if digits.startswith('380'):
            return '+' + digits
        elif digits.startswith('0'):
            return '+38' + digits
        else:
            return '+38' + digits

    @staticmethod
    def validate(value):
        return len(value) == 13 and value.startswith('+380')


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
