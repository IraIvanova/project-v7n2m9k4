from collections import UserDict
from datetime import datetime, timedelta
from assistant.models.field import Name, Phone, Email, Address, Birthday
from assistant.errors.exceptions import AddressBookError, InvalidPhoneError, FieldNotSetError


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None
        self.address = None
        self.is_favorite = False

    # Phones
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def edit_phone(self, old_phone, new_phone):
        phone = self.find_phone(old_phone)

        if phone is None:
            raise AddressBookError("Phone not found.")

        if not Phone.validate(new_phone):
            raise InvalidPhoneError("Phone must contain exactly 10 digits.")

        phone.value = new_phone

    def remove_phone(self, phone):
        p = self.find_phone(phone)
        if p:
            self.phones.remove(p)

    # Birthday
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    # Email
    def add_email(self, email):
        self.email = Email(email)

    def edit_email(self, email):
        if self.email is None:
            raise FieldNotSetError("Email not set.")
        self.email = Email(email)

    def delete_email(self):
        if self.email is None:
            raise FieldNotSetError("Email not set.")
        self.email = None

    # Address
    def add_address(self, address):
        self.address = Address(address)

    def edit_address(self, address):
        if self.address is None:
            raise FieldNotSetError("Address not set.")
        self.address = Address(address)

    def delete_address(self):
        if self.address is None:
            raise FieldNotSetError("Address not set.")
        self.address = None

    def mark_favorite(self):
        self.is_favorite = True

    def unmark_favorite(self):
        self.is_favorite = False

    def __str__(self):
        favorite_prefix = "⭐" if getattr(self, "is_favorite", False) else ""
        phones = "; ".join(str(p) for p in self.phones)
        birthday = f", birthday: {self.birthday}" if self.birthday else ""
        email = f", email: {self.email}" if self.email else ""
        address = f", address: {self.address}" if self.address else ""
        return f"Contact name: {favorite_prefix}{self.name}, phones: {phones}{birthday}{email}{address}"


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming = []

        for record in self.data.values():

            if record.birthday is None:
                continue

            birthday = record.birthday.value.date()
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            delta_days = (birthday_this_year - today).days

            if 0 <= delta_days <= 7:
                congrat_date = birthday_this_year

                if congrat_date.weekday() == 5:
                    congrat_date += timedelta(days=2)
                elif congrat_date.weekday() == 6:
                    congrat_date += timedelta(days=1)

                upcoming.append({
                    "name": record.name.value,
                    "congratulation_date": congrat_date.strftime("%d.%m.%Y")
                })

        return upcoming
