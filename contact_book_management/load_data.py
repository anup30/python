import os
import csv

fields = ["name", "phone number", "email", "address"]


def load_data_from_database(contacts):
    if os.path.exists("all_contacts.csv"):
        with open("all_contacts.csv", "r") as f:
            reader = csv.reader(f)
            data = list(reader)
            contacts.clear()
            for i in range(1, len(data)):  # skip first row, or use list slicing on data ?
                contacts.append(data[i])
                # contacts.append([data[i][0], int(data[i][1]), data[i][2], data[i][3]])
                # if phone is taken as int, it loses leading zero

            """
            for row in reader:
                contacts.append(row)  # includes first row
            """
        contacts.sort(key=lambda arr: arr[0].lower())  # sort by name=0, phone=1  # reverse=False
        # capitals are before smalls, capitalize the names ? ---------------------------------------

    else:
        print("all_contacts.csv file not found! try adding some contact(s)\n")
