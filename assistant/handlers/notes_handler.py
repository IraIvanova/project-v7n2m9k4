from assistant.validators import validate_args
from assistant.errors import notes_input_error
from assistant.utils import console, extract_text_and_tags, print_notes_table

@notes_input_error
def add_note(args, notes):
    validate_args(args, 1, "Please provide Note text.")
    
    text, tags = extract_text_and_tags(args)

    if not text:
        raise ValueError("Note text is required.")
    
    note = notes.add(text, tags)
    
    console(f"Note created with id {note.id}", "success")


@notes_input_error
def edit_note(args, notes):
    validate_args(args, 2, "Please provide Note ID and new text or/and new tags.")

    text, tags = extract_text_and_tags(args[1:])
    note = notes.find(args[0])
    note.edit(text, tags)

    console("Note updated.", "success")


@notes_input_error
def remove_note(args, notes):
    validate_args(args, 1, "Please provide Note ID.")
    notes.delete(args[0])
    console("Note deleted.", "success")


@notes_input_error
def remove_tag(args, notes):
    validate_args(args, 2, "Please provide Note ID and Tag")

    tag = args[1]
    note = notes.find(args[0]) 
    note.remove_tag(tag)

    console(f"Tag {tag} removed.", "success")


@notes_input_error
def search_notes(args, notes):
    validate_args(args, 2, "Please provide search field (id/note/tag) and query.")
    results = notes.search_by(args[0], args[1])
    print_notes_table(results)


@notes_input_error
def sort_notes(args, notes):
    validate_args(args, 2, "Please provide sort field (note/tag) and query (for note is 1/-1) (for tag <#tag1> <tag2>... ).")
    results = notes.sort_by(args[0], args[1:])
    print_notes_table(results)


@notes_input_error
def get_all_notes(args, notes):
    notes_list = notes.show_all()
    print_notes_table(notes_list)