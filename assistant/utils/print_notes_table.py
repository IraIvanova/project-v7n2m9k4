from .console import console
from tabulate import tabulate

def print_notes_table(notes):

    if not notes:
        console("No notes found.", "error")
        return

    table = []

    for note in notes:
        tags = " ".join(tag.value for tag in note.tags) if note.tags else "-"

        table.append([
            note.id,
            note.value,
            tags
        ])

    console(
        tabulate(
            table,
            headers=["NOTE ID", "NOTE TEXT", "NOTE TAGS"],
            tablefmt="fancy_grid"
        )
    )