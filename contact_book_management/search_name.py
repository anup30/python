fields = ["name", "phone number", "email", "address"]


def search_by_name(contacts):
    name = input("Enter the name you want to search in Contacts : ")
    found = False
    for i in range(0, len(contacts)):
        if name.lower() in contacts[i][0].lower():  # finds substring
            found = True
            print(f"{fields[0]} = {contacts[i][0]}, {fields[1]} = {contacts[i][1]}, {fields[2]} = {contacts[i][2]}, "
                  f"{fields[3]} = {contacts[i][3]}, ")
    print()

    if not found:
        print(f"'{name}' not found in Contacts!\n")

