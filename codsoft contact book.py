import json
import os

FILE = "contacts.json"

# -------- File Handling --------
def load_contacts():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=4)

# -------- Functions --------
def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    save_contacts(contacts)
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    for i, contact in enumerate(contacts, 1):
        print(f"""
{i}. Name: {contact['name']}
   Phone: {contact['phone']}
   Email: {contact['email']}
   Address: {contact['address']}
""")

def search_contact(contacts):
    keyword = input("Enter name or phone to search: ").lower()

    found = False
    for contact in contacts:
        if keyword in contact["name"].lower() or keyword in contact["phone"]:
            print(f"""
Name: {contact['name']}
Phone: {contact['phone']}
Email: {contact['email']}
Address: {contact['address']}
""")
            found = True

    if not found:
        print("Contact not found.")

def update_contact(contacts):
    name = input("Enter name to update: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contact["phone"] = input("New Phone: ")
            contact["email"] = input("New Email: ")
            contact["address"] = input("New Address: ")
            save_contacts(contacts)
            print("Contact updated successfully!")
            return

    print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter name to delete: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully!")
            return

    print("Contact not found.")

# -------- Main Program --------
contacts = load_contacts()

while True:
    print("""
 CONTACT BOOK MENU
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
""")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact(contacts)
    elif choice == "2":
        view_contacts(contacts)
    elif choice == "3":
        search_contact(contacts)
    elif choice == "4":
        update_contact(contacts)
    elif choice == "5":
        delete_contact(contacts)
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")