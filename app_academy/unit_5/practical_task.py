# The Contact Book

contacts = [
    {
        'name': 'Thabo',
        'phone': '+27748859343',
        'email': 'thabot@ereddfd.com'
    },
    {
            'name': 'Eve',
            'phone': '+27748845454',
            'email': 'eve@ereddfd.com'
    },
    {
            'name': 'John',
            'phone': '+27745769778',
            'email': 'jonnyboy@ereddfd.com'
    }
]

def add_contact(contact):
    contacts.append(contact)
    print(f"contact added:\n {contacts}")

def search_contact(name):
    for contact in contacts:
        if name in contact['name']:
            print(f"contact returned:\n {contact}")
            return contact
        else:
            print(f"No such contact found: {name}")
            return None
        
def delete_contact(name):
    for contact in contacts:
        if contact['name'] == name:
            print(f"contact deleted: {contact}")
            contacts.remove(contact)
            return

def view_all():
    for contact in contacts:
        print(contact)

while True:
    print("1=Add, \n2=Search, \n3=Delete, \n4=View All, \n5=Exit")
    command_number = int(input("Enter your command: "))

    if command_number == 1:
        name = input("Please enter the name: ")
        phone = input("Please enter the phone number: ")
        email = input("Please enter the email: ")
        add_contact({'name': name, 'phone': phone, 'email': email})
    elif command_number == 2:
        name = input("Please enter the name: ")
        search_contact(name)
    elif command_number == 3:
        name = input("Please enter the name: ")
        delete_contact(name)
    elif command_number == 4:
        view_all()
    elif command_number == 5:
        print("Goodbye!!!")
        break
    else:
        continue