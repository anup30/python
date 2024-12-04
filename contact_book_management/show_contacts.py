fields = ["name", "phone number", "email", "address"]


def show_all_contacts(contacts):
    if len(contacts) == 0:
        print("Contacts list is empty. try to add some\n")
        return
    print("Full contact list: ")
    print("   ", end="")
    for elem in fields:
        print(f"{elem}, ", end="")
    print()
    num = 1
    for row in contacts:
        print(f"{num}. ", end="")
        num += 1
        for ele in row:
            print(f"{ele}, ", end="")
        print()
    print()
