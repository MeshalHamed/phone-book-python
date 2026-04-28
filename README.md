# Phonebook CLI Application

A simple command-line phonebook application written in Python that stores contacts in a JSON file.

## Features

- **Add Contact** - Add new contacts with name and phone number
- **View Contacts** - Display all saved contacts
- **Remove Contact** - Delete a contact by selecting its number
- **Update Contact** - Edit existing contact information
- **Persistent Storage** - Contacts are saved to a JSON file and persist between sessions

## How to Run

```bash
python phonebook.py
```

## Requirements

- Python 3.x
- No external dependencies (uses built-in `json` module)

## Usage

1. Run the program
2. Choose an option from the menu (1-5)
3. Follow the prompts

### Menu Options

| Option | Action |
|--------|--------|
| 1 | Add a new contact |
| 2 | Show all contacts |
| 3 | Remove a contact |
| 4 | Update a contact |
| 5 | Exit the program |

## Project Structure

```
.
├── phonebook.py      # Main application code
├── phonebook.json    # Data file (created automatically)
└── README.md         # This file
```

## Code Overview

- `Contact` class - Represents a single contact with name and number
- `load_contacts()` - Loads contacts from JSON file
- `save_contacts()` - Saves contacts to JSON file
- `add_contact()` - Adds a new contact
- `remove_contact()` - Removes a contact
- `update_contact()` - Updates contact information
- `main()` - Main program loop

## License

MIT License
