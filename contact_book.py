import json
#creating class of contact
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"
#creating class of cintact manager
class ContactManager:
    def __init__(self):
        self.contacts = []

#Addition of contact no
    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added successfully.")

#Viewing contact list
    def view_contact_list(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact}")

#Search contact no 
    def search_contact(self, search_term):
        search_results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if not search_results:
            print("No matching contacts found.")
        else:
            for idx, contact in enumerate(search_results, start=1):
                print(f"{idx}. {contact}")

#to change or update contact
    def update_contact(self, contact_index, new_contact):
        if 1 <= contact_index <= len(self.contacts):
            self.contacts[contact_index - 1] = new_contact
            print("Contact updated successfully.")
        else:
            print("Invalid contact index.")

#to delete contact
    def delete_contact(self, contact_index):
        if 1 <= contact_index <= len(self.contacts):
            del self.contacts[contact_index - 1]
            print("Contact deleted successfully.")
        else:
            print("Invalid contact index.")

#saving file information
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            contacts_data = [{'name': contact.name, 'phone': contact.phone, 'email': contact.email, 'address': contact.address} for contact in self.contacts]
            json.dump(contacts_data, file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                contacts_data = json.load(file)
                self.contacts = [Contact(**data) for data in contacts_data]
        except FileNotFoundError:
            print("File not found. Starting with an empty contact list.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Save Contacts to File")
        print("7. Load Contacts from File")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")


        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone, email, address)
            contact_manager.add_contact(new_contact)

        elif choice == '2':
            contact_manager.view_contact_list()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_manager.search_contact(search_term)

        elif choice == '4':
            contact_manager.view_contact_list()
            contact_index = int(input("Enter the index of the contact to update: "))
            name = input("Enter new name: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            updated_contact = Contact(name, phone, email, address)
            contact_manager.update_contact(contact_index, updated_contact)

        elif choice == '5':
            contact_manager.view_contact_list()
            contact_index = int(input("Enter the index of the contact to delete: "))
            contact_manager.delete_contact(contact_index)

        elif choice == '6':
            filename = input("Enter the filename to save contacts: ")
            contact_manager.save_to_file(filename)

        elif choice == '7':
            filename = input("Enter the filename to load contacts from: ")
            contact_manager.load_from_file(filename)

        elif choice == '8':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
