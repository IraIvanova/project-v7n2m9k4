from assistant.handlers import contacts_handler, address_handler, emails_handler, birthdays_handler, notes_handler

COMMANDS = {
   # CONTACT COMMANDS
    "add-contact": contacts_handler.add_contact,
    "edit-contact": contacts_handler.edit_contact,
    "delete-contact": contacts_handler.remove_contact,
    "search-contact": contacts_handler.show_contact,
    "all-contacts": contacts_handler.get_all_contacts,

    "add-address": address_handler.add_address,
    "edit-address": address_handler.edit_address,
    "delete-address": address_handler.remove_address,
    "show-address": address_handler.show_address,

    "add-email": emails_handler.add_email,
    "edit-email": emails_handler.edit_email,
    "delete-email": emails_handler.remove_email,
    "show-email": emails_handler.show_email,

    "add-birthday": birthdays_handler.add_birthday,
    "edit-birthday": birthdays_handler.edit_birthday,
    "delete-birthday": birthdays_handler.remove_birthday,
    "show-birthday": birthdays_handler.show_birthday,
    "contacts-birthdays": birthdays_handler.get_upcoming_birthdays,

   # NOTES COMMANDS
    "add-note": notes_handler.add_note,
    "edit-note": notes_handler.edit_note,
    "delete-note": notes_handler.remove_note,
    "show-note": notes_handler.show_note,
    "search-notes": notes_handler.search_notes,
    "search-note-by-tag": notes_handler.search_notes_by_tag,
    "all-notes": notes_handler.get_all_notes,

    "add-tag": notes_handler.add_tag,
    "edit-tag": notes_handler.edit_tag,
    "delete-tag": notes_handler.remove_tag,
}