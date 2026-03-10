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
Examples may include:
- add note
- edit note
- remove note
- show notes
- search notes
- add tags to notes

### Additional field commands
Examples may include:
- add address
- edit address
- add birthday
- edit birthday
- add email
- edit email
