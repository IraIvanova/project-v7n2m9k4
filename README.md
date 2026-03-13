# 🤖 AmigoNotesBot

AmigoNotesBot is a console-based Python assistant for working with contacts and notes.  
The project is organized as a Python package and follows a modular structure so that command handling, validation, storage, models, and error processing stay separated and maintainable.

This README explains how to run the project correctly, how the codebase is structured, and how to extend it safely.

---

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Supported Commands](#supported-commands)

---

## ✨ Overview
The application is designed as a command-line assistant that can:

-  Create, edit, search, and delete contacts
-  Manage contact fields such as address, email, and birthday
-  Show upcoming birthdays
-  Create, edit, search, sort, and delete notes
-  Add and remove note tags
-  Search notes by different fields
-  Run the app directly from the terminal after installation

## Smart Command Analysis
The assistant features a two-level intelligent command recognition system to make the interaction seamless and user-friendly:

1. Real-time Autocompletion (Tab)
The bot "guesses" your intent as you type. By pressing the Tab key, the assistant will:
-  Complete the command if there is only one match.
-  Show a list of all available options if there are multiple matches (e.g., typing add- and pressing Tab twice).

2. Fuzzy Matching & Suggestions
If a command is entered with a typo or is incomplete (and the user presses Enter), the bot uses the Levenshtein distance algorithm to:

-  Analyze how close the input is to existing commands.
-  Suggest the most likely intended command (e.g., adres -> add-address).
-  Provide a helpful hint to use the help command if the input is completely unrecognizable.

---
## 📂 Project Structure
The project is structured as a Python package:

```text
assistant/
│
├── commands/ # Command mapping and command resolution
├── errors/ # Custom exceptions and error handling
├── handlers/ # Logic for contacts, notes, emails, addresses, and birthdays
├── models/ # Core data models
├── storage/ # Data persistence
├── utils/ # Console utilities and table rendering helpers
├── validators/ # Input and data validation
│
├── main.py # Main application loop
└── __main__.py # Entry point for python -m assistant

pyproject.toml # Package configuration and CLI entry setup
requirements.txt # Dependency list
```
---
## ⚙️ Requirements

- **Python 3.9+**
- `pip`
- `venv` module available in your Python installation

### Dependencies
- colorama
- tabulate
- prompt_toolkit
- thefuzz
- rapidfuzz

---

## 🛠️ Project Setup

Follow these steps from the **project root directory**.

---

### 1. Create a Virtual Environment

```bash
python -m venv .venv
```

---

### 2. Activate the virtual environment

On **Linux / macOS**:
```bash
source .venv/bin/activate
```

On **Windows (PowerShell)**:
```bash
powershell .venv\Scripts\Activate.ps1
```

---

### 3. Upgrade `pip` (recommended)
```bash
python -m pip install --upgrade pip
```

---

### 4. Install the project
```bash
pip install .
```

This will install the current project as a local package using the configuration from `pyproject.toml`.

This also makes the CLI command available:
```bash
assistant 
```
---
## 💡 Basic Usage

After starting the application, you can type commands directly in the terminal.

Example:

```text
Enter a command: add-contact John 1234567890
```
## Supported Commands
## 📇 Contact Commands

| Command                                                                      | Description                                                 |
|------------------------------------------------------------------------------|-------------------------------------------------------------|
| `add-contact <name> <phone>`                                                 | Creates a new contact with the given name and phone number. |
| `delete-contact <name>`                                                      | Deletes a contact by name.                                  |
| `search-contacts <field> <query> (field: name/phone/email/birthday/address)` | Searches for a contact by a query value.                    |
| `mark-favorite <name>`                                                       | Marks a contact as favorite.                                |
| `unmark-favorite <name>`                                                     | Removes the favorite mark from a contact.                   |
| `favorite-contacts`                                                          | Shows all contacts marked as favorite.                      |
| `all-contacts`                                                               | Displays all saved contacts.                                |
| `add-phone <name> <phone>`                                                   | Add new phone number to a contact.                          |
| `edit-phone <name> <old_phone> <new_phone>`                                  | Updates a contact’s phone number.                           |

---
## 📝 Note Commands
The assistant supports managing notes with tags. Each note contains:

1. **ID** - unique identifier generated automatically
1. **TEXT** - the content of the note
1. **TAGS** - optional tags starting with `#`


| Command                                                                    | Description |
|----------------------------------------------------------------------------|-------------|
| `add-note <text> [#tag1 #tag2 ...]`                                        | Creates a new note with optional tags. |
| `edit-note <note_id> <new text> [#tag1 #tag2 ...]`                         | Edits an existing note by its ID. |
| `delete-note <note_id>`                                                    | Deletes a note by its ID. |
| `search-notes <field> <query> (field: id/note/tag)`                        | Searches notes using a field and query value. |
| `sort-notes <field> <query> (field: note/tag) (note: 1/-1, tag: #tag1 #tag2...)` | Sorts or filters notes depending on the field and query provided. |
| `all-notes`                                                                | Displays all saved notes. |
| `delete-tag <note_id> <#tag>`                                             | Removes a tag from a note by note ID. |

## 🏠 Address Commands

| Command | Description |
|--------|-------------|
| `add-address <name> <address>` | Adds an address to a contact. |
| `edit-address <name> <new address>` | Updates the address of a contact. |
| `delete-address <name>` | Removes the address from a contact. |
| `show-address <name>` | Displays the saved address for a contact. |

---

## 📧 Email Commands

| Command | Description |
|--------|-------------|
| `add-email <name> <email>` | Adds an email address to a contact. |
| `edit-email <name> <email>` | Updates a contact’s email address. |
| `delete-email <name>` | Removes the email address from a contact. |
| `show-email <name>` | Displays the saved email for a contact. |

---

## 🎂 Birthday Commands

| Command | Description |
|--------|-------------|
| `add-birthday <name> <birthday>` | Adds a birthday to a contact. |
| `edit-birthday <name> <birthday>` | Updates a contact’s birthday. |
| `delete-birthday <name>` | Removes a birthday from a contact. |
| `show-birthday <name>` | Displays the saved birthday for a contact. |
| `contacts-birthdays` | Shows upcoming birthdays for saved contacts. |

---

## ⚙️ System Commands

| Command         | Description |
|-----------------|------------|
| `hello`, `hi`      | Prints a greeting response. |
| `help`          | Displays the built-in help table with available commands. |
| `exit`, `close` | Closes the application. |
