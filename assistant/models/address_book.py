from field import Field
from collections import UserDict


class Name(Field):
    def validate(self):
        pass


class Phone(Field):
    def validate(self):
        pass


class Birthday(Field):
    def validate(self):
        pass

class Email(Field):
    def validate(self):
        pass

class Record:
    def __init__(self):
        pass

    def add_phone(self):
       pass

    def edit_phone(self):
        pass

    def remove_phone(self):
        pass

    def find_phone(self):
        pass

    def add_birthday(self):
        pass

    def add_email(self):
        pass

    def edit_email(self):
        pass

    def __str__(self):
        pass


class AddressBook(UserDict):
    def add_record(self):
        pass

    def find(self):
       pass

    def delete(self):
        pass

    def validate(self):
        pass

    def show_all(self):
        pass


    def get_upcoming_birthdays(self):
        pass

    def search(self):
        pass
