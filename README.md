# AmigoNotesBot

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

## Overview

The application is designed as a command-line assistant that can:

- manage contacts
- manage notes
- validate input data
- save and load application data
- organize functionality into clear layers

---

TODO: add info about structure

---

## Requirements

- Python 3.14 or newer
- standard Python environment

## How to Run

### 1. Open the project root

Navigate to the folder that contains the `assistant` package:

### 2. Run the package as a module

`python -m assistant`

## Supported Commands

### General commands

- `hello`
- `hi`
- `close`
- `exit`

### Contact-related commands

- add-contact
- edit-contact
- remove-contact
- show-contact
- list contacts
- search contacts

### Note-related commands

The assistant supports managing notes with tags. Each note contains:

1. **ID** - unique identifier generated automatically
1. **TEXT** - the content of the note
1. **TAGS** - optional tags starting with `#`

use related commands like:

- add-note <**text**> [#tag1 #tag2 ...]
- edit-note <**note_id**> <**new text**> [#tag1 #tag2 ...]
- delete-note <**note_id**>
- delete-tag <**note_id**> <**#tag**>
- search-notes <**field**> <**query**> (field: id/note/tag)
- sort-notes <**field**> <**query**> (field: note/tag) (note: 1/-1, tag: #tag1 #tag2...)
- all-notes

### Additional field commands

Examples may include:

- add address
- edit address
- add birthday
- edit birthday
- add email
- edit email
