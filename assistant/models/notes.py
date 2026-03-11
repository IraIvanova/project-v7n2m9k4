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
            existing_tags = {tag.value for tag in self.tags}

            for tag in new_tags:
                if tag not in existing_tags:
                    self.tags.append(Tag(tag))

    # REMOVE TAG FROM NOTE
    def remove_tag(self, tag):

        if not tag.startswith("#"):
            tag = f"#{tag}"

        for t in self.tags:
            if t.value.lower() == tag.lower():
                self.tags.remove(t)
                return

        raise ValueError("Tag not found.")

    def __str__(self):
        return self.value

class NotesList(UserDict):
    # ADD NOTE
    def add(self, text, tags=None):
        tags = [Tag(tag) for tag in tags] if tags else []

        note = Note(text, tags)
        self.data[note.id] = note

        return note
    
    # FIND NOTE BY ID
    def find(self, note_id):
        note = self.data.get(note_id)

        if not note:
            raise ValueError("Note not found.")

        return note

    # DELETE NOTE
    def delete(self, note_id):
        note = self.data.pop(note_id, None)

        if not note:
            raise ValueError("Note not found.")
        
        return note

    # SEARCH NOTE BY CUSTOM FIELD
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
                if not query.startswith("#"):
                    query = f"#{query}"

                for tag in note.tags:
                    if query.lower() == tag.value.lower():
                        results.append(note)
                        break

            else:
                raise ValueError("Invalid field name. You can use only id/note/tag")

        return results
    
    # SORT NOTE BY CUSTOM FIELD
    def sort_by(self, field, query):
        notes = list(self.data.values())

        if field == "note":
            reverse = "-1" in query
            return sorted(notes, key=lambda n: n.value.lower(), reverse=reverse)

        elif field == "tag":
            if isinstance(query, str):
                query = [query]

            sorted_notes = []
            used = set()

            for tag in query:

                if not tag.startswith("#"):
                    tag = f"#{tag}"

                for note in notes:

                    if note.id in used:
                        continue

                    if any(t.value.lower() == tag.lower() for t in note.tags):
                        sorted_notes.append(note)
                        used.add(note.id)

            for note in notes:
                if note.id not in used:
                    sorted_notes.append(note)

            return sorted_notes

        else:
            raise ValueError("Invalid field name. Use note/tag.")

    # SHOW_ALL NOTES
    def show_all(self):
        return list(self.data.values())
