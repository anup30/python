import csv
fields = ["name", "phone number", "email", "address"]


def remove_entry(contacts):
    phone = input("Phone number of the contact to delete : ")
    index = -1
    for i in range(0, len(contacts)):
        if contacts[i][1] == phone:
            index = i
            break

    if index != -1:
        name = contacts[index][0]
        contacts.pop(index)
        with open("all_contacts.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(fields)
            writer.writerows(contacts)
        print(f"Contact removed, with name: {name}, phone number: {phone}\n")
    else:
        print(f"nothing to remove! the number {phone} is not present in contact list.")
