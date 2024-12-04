import show_contacts
import add_contact
import remove_contact
import search_name


def print_info():
    print("Select an option from below :")
    print("1. View all Contact Lists")
    print("2. Add a New Contact")  # duplicate phone numbers are not added
    print("3. Search Contact by Name")  # finds if present as substring
    print("4. Remove a Contact by Phone NUmber")
    print("0. Quit App")
    print()


def option_selection(contacts):
    while True:
        print_info()
        select = input("Your choice is : ")
        if select == "0":
            print("Thank You for using Contact Book Management System")
            break
        elif select == "1":
            show_contacts.show_all_contacts(contacts)
        elif select == "2":
            add_contact.add_new(contacts)
        elif select == "3":
            search_name.search_by_name(contacts)
        elif select == "4":
            remove_contact.remove_entry(contacts)
        else:
            print("Invalid input, try agin")
