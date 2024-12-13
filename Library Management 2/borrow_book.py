import json
from datetime import datetime, timedelta


def borrow_a_book(all_books, borrower_list):
    print('In order to borrow a book provide Book and Author name to check if it is available:')
    book_name = input("Enter Book title : ")
    author_name = input("Enter Author name : ")
    found = False
    index = -1
    for i in range(0, len(all_books)):
        if all_books[i]['title'].lower() == book_name.lower() and all_books[i]['author'].lower() == author_name.lower():
            found = True
            index = i
            break
    if found:
        if all_books[index]['quantity'] > 0:
            print('the Book found in database')
            while True:
                try:
                    user_name = input('Enter your name : ')
                    user_phone = input('Enter your phone number : ')
                    days1 = int(input('For how many days you want to borrow : '))
                    t1 = datetime.now()
                    rt = t1 + timedelta(days=days1)
                    return_time = rt.strftime("%d-%m-%Y %H:%M:%S")
                    break
                except Exception as e:
                    print("Error :", e, "try again")

            borrow_data = {
                "name": user_name,
                "phone": user_phone,
                "return_time": return_time,
                "book_title": all_books[index]['title'],
                "book_author": all_books[index]['author'],
            }
            all_books[index]['quantity'] -= 1  # reduce quantity by 1
            all_books[index]['borrowed'] += 1
            borrower_list.append(borrow_data)
            # borrower_list.sort(key=lambda x: (x['name'], x['phone']))  # keep sorted
            with open("all_books.json", "w") as fp:
                json.dump(all_books, fp, indent=4)
            with open("all_borrowers.json", "w") as fp:
                json.dump(borrower_list, fp, indent=4)
            print(f'{user_name} borrowed {all_books[index]['title']} successfully\n')

        else:
            print("Currently all books are borrowed. try again latter. thank you\n")  # stock/quantity is 0

    else:
        print('The provided title and author combination was not found in Database!\n')

