import json


class Contact:
    """Represents a single contact in the phonebook."""
    
    def __init__(self, name, number):
        self.name = name
        self.number = number

    @classmethod
    def from_input(cls):
        """Create a new contact from user input."""
        name = input("Enter the contact name: ")
        number = input("Enter the contact number: ")
        return cls(name, number)


# ==================== File Operations ====================

def load_contacts():
    """Load contacts from JSON file."""
    contacts = []
    try:
        with open("phonebook.json", "r") as f:
            data = json.load(f)
            for entry in data:
                contacts.append(Contact(entry["name"], entry["number"]))
    except FileNotFoundError:
        pass
    return contacts


def save_contacts(contacts):
    """Save all contacts to JSON file."""
    with open("phonebook.json", "w") as f:
        json.dump([contact.__dict__ for contact in contacts], f, indent=2)


# ==================== Contact Operations ====================

def show_contacts(contacts):
    """Display all contacts."""
    if not contacts:
        print("No contacts in the phonebook.")
        return
    
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact.name} - {contact.number}")


def add_contact(contacts):
    """Add a new contact."""
    new_contact = Contact.from_input()
    contacts.append(new_contact)
    save_contacts(contacts)
    print(f"Added {new_contact.name} - {new_contact.number}")


def remove_contact(contacts):
    """Remove a contact by number."""
    show_contacts(contacts)
    if not contacts:
        return
    
    try:
        choice = int(input("Enter the number of the contact to remove: ")) - 1
        if 0 <= choice < len(contacts):
            removed = contacts.pop(choice)
            print(f"Removed {removed.name}")
            save_contacts(contacts)
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")


def update_contact(contacts):
    """Update an existing contact."""
    show_contacts(contacts)
    if not contacts:
        return
    
    try:
        choice = int(input("Enter the number of the contact to update: ")) - 1
        if 0 <= choice < len(contacts):
            contact = contacts[choice]
            print(f"Updating {contact.name} - {contact.number}")
            
            new_name = input("Enter the new name (leave blank to keep current): ")
            new_number = input("Enter the new number (leave blank to keep current): ")
            
            if new_name:
                contact.name = new_name
            if new_number:
                contact.number = new_number
            
            print(f"Updated to {contact.name} - {contact.number}")
            save_contacts(contacts)
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")


# ==================== Main Menu ====================

def show_menu():
    """Display the main menu."""
    print("\n--- Phonebook Menu ---")
    print("1. Add Contact")
    print("2. Show Contacts")
    print("3. Remove Contact")
    print("4. Update Contact")
    print("5. Exit")


def main():
    """Main program entry point."""
    print("Welcome to the Phonebook!")
    contacts = load_contacts()
    
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            show_contacts(contacts)
        elif choice == "3":
            remove_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()