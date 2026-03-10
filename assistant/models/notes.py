from collections import UserDict
from field import Field

class Tag(Field):
   def validate(self):
       pass

class Note(Field):
    def validate(self):
        pass

class NotesList(UserDict):
    def add_note(self):
        pass

    def edit_note(self):
        pass

    def delete_note(self):
        pass

    def add_tag(self):
        pass

    def remove_tag(self):
        pass

    def search(self):
        pass

    def show_all(self):
        pass
