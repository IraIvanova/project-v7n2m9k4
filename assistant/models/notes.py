import uuid
from collections import UserDict
from .field import Field

class Tag(Field):
    def validate(self):
        if not self.value.startswith("#"):
            raise ValueError("Tag must start with #")

class Note(Field):
    def __init__(self, value, tags=None):
        super().__init__(value)
        self.id = str(uuid.uuid4())[:8]
        self.tags = tags or []

    def validate(self):
        if not self.value:
            raise ValueError("Note text cannot be empty")
        
    # EDIT NOTE   
    def edit(self, new_text=None, new_tags=None):

        if not new_text and not new_tags:
            raise ValueError("Nothing to update.")

        if new_text:
            self.value = new_text.strip()

        if new_tags:
            for tag in new_tags:
                tag_obj = Tag(tag)
                if tag_obj not in self.tags:
                    self.tags.append(tag_obj)

    # REMOVE TAG FROM NOTE
    def remove_tag(self, tag):

        for t in self.tags:
            if t.value == tag:
                self.tags.remove(t)
                return

        raise ValueError("Tag not found.")

    def __str__(self):
        return self.value

class NotesList(UserDict):
    # ADD NOTE
    def add(self, text, tags=None):
        note = Note(text, tags)
        self.data[note.id] = note

        return note
    
    # DELETE NOTE
    def delete(self, note_id):
        note = self.data.pop(note_id, None)

        if not note:
            raise ValueError("Note not found.")
        
        return note

    # SEARCH NOTE BY FIELD NAME
    def search_by(self, field, query):
        results = []

        for note in self.data.values():

            if field == "id":
                if query in note.id:
                    results.append(note)

            elif field == "note":
                if query.lower() in note.value.lower():
                    results.append(note)

            elif field == "tag":
                for tag in note.tags:
                    if query.lower() in tag.value.lower():
                        results.append(note)
                        break

            else:
                raise ValueError("Invalid search field.")

        return results
    
    # SHOW_ALL NOTES
    def show_all(self):
        return list(self.data.values())
