from assistant.handlers import contacts_handler, address_handler, emails_handler, birthdays_handler, notes_handler

COMMANDS = {
   # CONTACT COMMANDS
    "add-contact": {
        "handler": contacts_handler.add_contact,
        "entity": "contact"
    },
    "edit-contact": {
        "handler": contacts_handler.edit_contact,
        "entity": "contact"
    },
    "delete-contact": {
        "handler": contacts_handler.remove_contact,
        "entity": "contact"
    },
    "search-contact": {
        "handler": contacts_handler.show_contact,
        "entity": "contact"
    },
    "all-contacts": {
        "handler": contacts_handler.get_all_contacts,
        "entity": "contact"
    },
    "add-address": {
        "handler": address_handler.add_address,
        "entity": "contact"
    },
    "edit-address": {
        "handler": address_handler.edit_address,
        "entity": "contact"
    },
    "delete-address": {
        "handler": address_handler.remove_address,
        "entity": "contact"
    },
    "show-address": {
        "handler": address_handler.show_address,
        "entity": "contact"
    },

    "add-email":  {
        "handler": emails_handler.add_email,
        "entity": "contact"
    },
    "edit-email": {
        "handler": emails_handler.edit_email,
        "entity": "contact"
    },
    "delete-email": {
        "handler": emails_handler.remove_email,
        "entity": "contact"
    },
    "show-email": {
        "handler": emails_handler.show_email,
        "entity": "contact"
    },

    "add-birthday": {
        "handler": birthdays_handler.add_birthday,
        "entity": "contact"
    },
    "edit-birthday": {
        "handler": birthdays_handler.edit_birthday,
        "entity": "contact"
    },
    "delete-birthday": {
        "handler": birthdays_handler.remove_birthday,
        "entity": "contact"
    },
    "show-birthday": {
        "handler": birthdays_handler.show_birthday,
        "entity": "contact"
    },
    "contacts-birthdays": {
        "handler": birthdays_handler.get_upcoming_birthdays,
        "entity": "contact"
    },

   # NOTES COMMANDS
    "add-note": {
        "handler": notes_handler.add_note,
        "entity": "contact"
    },
    "edit-note": {
        "handler": notes_handler.edit_note,
        "entity": "contact"
    },
    "delete-note": {
        "handler": notes_handler.remove_note,
        "entity": "contact"
    },
    "show-note": {
        "handler": notes_handler.show_note,
        "entity": "contact"
    },
    "search-notes": {
        "handler": notes_handler.search_notes,
        "entity": "contact"
    },
    "search-note-by-tag": {
        "handler": notes_handler.search_notes_by_tag,
        "entity": "contact"
    },
    "all-notes": {
        "handler": notes_handler.get_all_notes,
        "entity": "contact"
    },

    "add-tag": {
        "handler": notes_handler.add_tag,
        "entity": "contact"
    },
    "edit-tag":{
        "handler": notes_handler.edit_tag,
        "entity": "contact"
    },
    "delete-tag": {
        "handler": notes_handler.remove_tag,
        "entity": "contact"
    },
}