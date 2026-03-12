from assistant.handlers import (
    add_contact, edit_contact, remove_contact, show_contact, get_all_contacts,
    add_phone, edit_phone, remove_phone, show_phones,
    add_address, edit_address, remove_address, show_address,
    add_email, edit_email, remove_email, show_email,
    add_birthday, edit_birthday, remove_birthday, show_birthday, get_upcoming_birthdays,
    add_note, edit_note, remove_note, search_notes, get_all_notes,
    remove_tag, sort_notes,
)

COMMANDS = {
   # CONTACT COMMANDS
    "add-contact": {
        "handler": add_contact,
        "entity_type": "contacts"
    },
    "edit-contact": {
        "handler": edit_contact,
        "entity_type": "contacts"
    },
    "delete-contact": {
        "handler": remove_contact,
        "entity_type": "contacts"
    },
    "search-contact": {
        "handler": show_contact,
        "entity_type": "contacts"
    },
    "all-contacts": {
        "handler": get_all_contacts,
        "entity_type": "contacts"
    },
    "add-address": {
        "handler": add_address,
        "entity_type": "contacts"
    },
    "edit-address": {
        "handler": edit_address,
        "entity_type": "contacts"
    },
    "delete-address": {
        "handler": remove_address,
        "entity_type": "contacts"
    },
    "show-address": {
        "handler": show_address,
        "entity_type": "contacts"
    },

    "add-email":  {
        "handler": add_email,
        "entity_type": "contacts"
    },
    "edit-email": {
        "handler": edit_email,
        "entity_type": "contacts"
    },
    "delete-email": {
        "handler": remove_email,
        "entity_type": "contacts"
    },
    "show-email": {
        "handler": show_email,
        "entity_type": "contacts"
    },

    "add-birthday": {
        "handler": add_birthday,
        "entity_type": "contacts"
    },
    "edit-birthday": {
        "handler": edit_birthday,
        "entity_type": "contacts"
    },
    "delete-birthday": {
        "handler": remove_birthday,
        "entity_type": "contacts"
    },
    "show-birthday": {
        "handler": show_birthday,
        "entity_type": "contacts"
    },
    "contacts-birthdays": {
        "handler": get_upcoming_birthdays,
        "entity_type": "contacts"
    },
    "add-phone": {
        "handler": add_phone,
        "entity_type": "contacts"
    },
    "edit-phone": {
        "handler": edit_phone,
        "entity_type": "contacts"
    },
    "delete-phone": {
        "handler": remove_phone,
        "entity_type": "contacts"
    },
    "show-phones": {
        "handler": show_phones,
        "entity_type": "contacts"
    },

   # NOTES COMMANDS
    "add-note": {
        "handler": add_note,
        "entity_type": "notes"
    },
    "edit-note": {
        "handler": edit_note,
        "entity_type": "notes"
    },
    "delete-note": {
        "handler": remove_note,
        "entity_type": "notes"
    },
    "search-notes": {
        "handler": search_notes,
        "entity_type": "notes"
    },
    "sort-notes": {
        "handler": sort_notes,
        "entity_type": "notes"
    },
    "all-notes": {
        "handler": get_all_notes,
        "entity_type": "notes"
    },
    "delete-tag": {
        "handler": remove_tag,
        "entity_type": "notes"
    },
}
