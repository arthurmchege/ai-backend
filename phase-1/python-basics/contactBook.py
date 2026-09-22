import json

class Contact():
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def newContact(self, name, phone, email):
        try:
            with open("contacts.json", "r") as f:
                existing_contacts = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_contacts = {}
        contact = Contact(name, phone, email)
        
        existing_contacts[name]= {"phone": phone, "email": email}
        with open("contacts.json", "w") as f:
            json.dump(existing_contacts, f)
            return f"Contact {contact.name} saved successfully."

        def findContact(self, name):
            try:
                with open("contacts.json", "r") as f:
                    loaded_data = json.load(f)
                    if  findContact.name == {name}:
                        return f"Contact {name} found: {loaded_data}"
            except:
                print("Contact not found")
            print(loaded_data)


name = input("Enter your name: ")
phone = input("Enter your phone number: ")
email = input("Enter your email: ")

add_contact = Contact(name, phone, email)
print(add_contact.newContact(name, phone, email))