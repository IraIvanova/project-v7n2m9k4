import pickle
from pathlib import Path
from assistant.models import AddressBook, NotesList

DATA_DIR = Path.home() / ".amigo_personal_assistant"
CONTACTS_FILE = DATA_DIR / "contacts.pkl"
NOTES_FILE = DATA_DIR / "notes.pkl"

def load_data():
    DATA_DIR.mkdir(exist_ok=True)

    if CONTACTS_FILE.exists():
        with open(CONTACTS_FILE, "rb") as f:
            contacts = pickle.load(f)
    else:
        contacts = AddressBook()

    if NOTES_FILE.exists():
        with open(NOTES_FILE, "rb") as f:
            notes = pickle.load(f)
    else:
        notes = NotesList()

    return contacts, notes


def save_data(contacts, notes):
    DATA_DIR.mkdir(exist_ok=True)

    with open(CONTACTS_FILE, "wb") as f:
        pickle.dump(contacts, f)

    with open(NOTES_FILE, "wb") as f:
        pickle.dump(notes, f)
