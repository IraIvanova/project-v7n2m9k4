from .console import console
from tabulate import tabulate

def print_contacts_table(contacts):

    if not contacts:
        console("No contacts found.", "error")
        return

    table = []

    for contact in contacts:
        phones = ",\n".join(tag.value for tag in contact.phones)

        table.append([
            contact.name,
            phones,
            contact.birthday or "-",
            contact.email or "-",
            contact.address  or "-",
        ])

    console(
        tabulate(
            table,
            headers=["NAME", "PHONE", "BIRTHDAY", "EMAIL", "ADDRESS"],
            tablefmt="fancy_grid"
        )
    )