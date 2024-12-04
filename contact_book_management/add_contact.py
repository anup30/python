import csv

fields = ["name", "phone number", "email", "address"]


def input_contact():
    new_entry = {}
    print("Enter your details, name must start with a letter")
    error = False
    try:
        new_entry = {
            "name": input("Your Name : "),
            "phone number": input("Your phone number : "),
            "email": input("Your email : "),
            "address": input("Your address : ")
        }
        if not new_entry["name"][0].isalpha():
            raise ValueError('name did not start with a letter.')
        if not new_entry["phone number"].isnumeric():
            raise ValueError('phone number is not numeric.')

    except ValueError as e:
        error = True
        print("Error:", e, "try again\n")
    finally:
        if not error:
            return list(new_entry.values())
        else:
            return None


def is_present_already(contacts, new_contact):
    found = False
    for i in range(0, len(contacts)):
        if contacts[i][1] == new_contact[1]:
            found = True
            break
    return found


def add_new(contacts):
    new_contact = input_contact()
    if new_contact is None:
        return
    if is_present_already(contacts, new_contact):
        print("Could not add contact. because Phone number already exits in Contacts list.\n")
        return
    contacts.append(new_contact)
    contacts.sort(key=lambda arr: arr[0].lower())  # sort contacts by name
    with open("all_contacts.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        writer.writerows(contacts)

    print("Contact added to List!\n")
