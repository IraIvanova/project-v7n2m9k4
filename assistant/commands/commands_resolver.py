from assistant.handlers import (
    add_contact, edit_contact, remove_contact, show_contact, get_all_contacts,
    add_address, edit_address, remove_address, show_address,
    add_email, edit_email, remove_email, show_email,
    add_birthday, edit_birthday, remove_birthday, show_birthday, get_upcoming_birthdays,
    add_note, edit_note, remove_note, show_note, search_notes, search_notes_by_tag, get_all_notes,
    add_tag, edit_tag, remove_tag
)

COMMANDS = {
   # CONTACT COMMANDS
    "add-contact": {
        "handler": add_contact,
        "entity_type": "contact"
    },
    "edit-contact": {
        "handler": edit_contact,
        "entity_type": "contact"
    },
    "delete-contact": {
        "handler": remove_contact,
        "entity_type": "contact"
    },
    "search-contact": {
        "handler": show_contact,
        "entity_type": "contact"
    },
    "all-contacts": {
        "handler": get_all_contacts,
        "entity_type": "contact"
    },
    "add-address": {
        "handler": add_address,
        "entity_type": "contact"
    },
    "edit-address": {
        "handler": edit_address,
        "entity_type": "contact"
    },
    "delete-address": {
        "handler": remove_address,
        "entity_type": "contact"
    },
    "show-address": {
        "handler": show_address,
        "entity_type": "contact"
    },

    "add-email":  {
        "handler": add_email,
        "entity_type": "contact"
    },
    "edit-email": {
        "handler": edit_email,
        "entity_type": "contact"
    },
    "delete-email": {
        "handler": remove_email,
        "entity_type": "contact"
    },
    "show-email": {
        "handler": show_email,
        "entity_type": "contact"
    },

    "add-birthday": {
        "handler": add_birthday,
        "entity_type": "contact"
    },
    "edit-birthday": {
        "handler": edit_birthday,
        "entity_type": "contact"
    },
    "delete-birthday": {
        "handler": remove_birthday,
        "entity_type": "contact"
    },
    "show-birthday": {
        "handler": show_birthday,
        "entity_type": "contact"
    },
    "contacts-birthdays": {
        "handler": get_upcoming_birthdays,
        "entity_type": "contact"
    },

   # NOTES COMMANDS
    "add-note": {
        "handler": add_note,
        "entity_type": "contact"
    },
    "edit-note": {
        "handler": edit_note,
        "entity_type": "contact"
    },
    "delete-note": {
        "handler": remove_note,
        "entity_type": "contact"
    },
    "show-note": {
        "handler": show_note,
        "entity_type": "contact"
    },
    "search-notes": {
        "handler": search_notes,
        "entity_type": "contact"
    },
    "search-note-by-tag": {
        "handler": search_notes_by_tag,
        "entity_type": "contact"
    },
    "all-notes": {
        "handler": get_all_notes,
        "entity_type": "contact"
    },

    "add-tag": {
        "handler": add_tag,
        "entity_type": "contact"
    },
    "edit-tag":{
        "handler": edit_tag,
        "entity_type": "contact"
    },
    "delete-tag": {
        "handler": remove_tag,
        "entity_type": "contact"
    },
}
