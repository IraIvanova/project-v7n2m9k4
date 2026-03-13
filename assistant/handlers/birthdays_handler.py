from assistant.errors.errors_handler import input_error
from assistant.errors.exceptions import AddressBookError
from assistant.validators import validate_args
from assistant.utils.contact_utils import get_contact_or_raise



@input_error
def add_birthday(args, book):
    validate_args(args, 2, "Please provide name and birthday.")
    name, birthday = args
    record = get_contact_or_raise(book, name)
    if record.birthday is not None:
        raise AddressBookError("Birthday already set. Use edit-birthday to change it.")
    record.add_birthday(birthday)
    return "Birthday added."


@input_error
def edit_birthday(args, book):
    validate_args(args, 2, "Please provide name and birthday.")
    name, birthday = args
    record = get_contact_or_raise(book, name)
    record.add_birthday(birthday)
    return "Birthday updated."


@input_error
def remove_birthday(args, book):
    validate_args(args, 1, "Please provide name.")
    record = get_contact_or_raise(book, args[0])
    record.birthday = None
    return "Birthday deleted."


@input_error
def show_birthday(args, book):
    validate_args(args, 1, "Please provide name.")
    record = get_contact_or_raise(book, args[0])
    if record.birthday is None:
        return "Birthday not set."
    return str(record.birthday)

@input_error
def get_upcoming_birthdays(args, book):
    # Якщо аргументи передані, валідуємо їх (очікуємо 1 аргумент - кількість днів)
    # Якщо аргументів немає, використовуємо значення за замовчуванням 7
    days = 7
    if args:
        # Перевіряємо наявність мінімум 1 аргументу та виводимо повідомлення при помилці
        validate_args(args, expected_count=1, message="Please provide a valid number of days.")
        try:
            days = int(args[0])
        except ValueError:
            raise ValueError("Please provide a valid number of days.")
    
    upcoming = book.get_upcoming_birthdays(days)
    
    if not upcoming:
        return f"No upcoming birthdays in the next {days} days."
    
    return "\n".join(f"{item['name']} - {item['congratulation_date']}" for item in upcoming)