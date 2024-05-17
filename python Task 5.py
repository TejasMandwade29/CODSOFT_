class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if self.contacts:
            print("Contacts:")
            for i, contact in enumerate(self.contacts):
                print(f"{i + 1}. Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")
        else:
            print("No contacts to display.")

    def search_contact(self, name):
        found_contacts = []
        for contact in self.contacts:
            if name.lower() in contact.name.lower():
                found_contacts.append(contact)
        if found_contacts:
            print("Found Contacts:")
            for i, contact in enumerate(found_contacts):
                print(f"{i + 1}. Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")
        else:
            print("No contacts found.")

    def update_contact(self, name, new_phone_number, new_email):
        for contact in self.contacts:
            if name.lower() == contact.name.lower():
                contact.phone_number = new_phone_number
                contact.email = new_email
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if name.lower() == contact.name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print(" Contact Book ")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact = Contact(name, phone_number, email)
            print("\n==============")
            contact_book.add_contact(contact)
            print("==============")
        elif choice == "2":
            print("\n==============")
            contact_book.view_contacts()
            print("==============")
        elif choice == "3":
            name = input("Enter name to search: ")
            print("\n==============")
            contact_book.search_contact(name)
            print("==============")
        elif choice == "4":
            name = input("Enter name to update: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            print("\n==============")
            contact_book.update_contact(name, new_phone_number, new_email)
            print("==============")
        elif choice == "5":
            name = input("Enter name to delete: ")
            print("\n==============")
            contact_book.delete_contact(name)
            print("==============")
        

if __name__ == "__main__":
    main()
