import borrowers
import json


def return_book(all_books, all_borrowers):
    sz = len(all_borrowers)
    if sz == 0:
        print("The borrowers list is empty, no books to return!")
        return
    print("from the borrowers list, select which one to return:")
    borrowers.show_borrowers_list(all_borrowers)
    while True:
        try:
            choice = int(input('your choice : '))
            if not 1 <= choice <= sz:
                raise ValueError("Choice out of range.")
            break
        except Exception as e:
            print("Error :", e, 'try again')
    user_name = all_borrowers[choice - 1]['name']
    book_name = all_borrowers[choice - 1]['book_title']
    book_author = all_borrowers[choice - 1]['book_author']
    all_borrowers.pop(choice - 1)
    for i in range(0, len(all_books)):
        if all_books[i]['title'] == book_name and all_books[i]['author'] == book_author:
            all_books[i]['quantity'] += 1
            all_books[i]['borrowed'] -= 1
    with open("all_borrowers.json", "w") as fp:
        json.dump(all_borrowers, fp, indent=4)
    with open("all_books.json", "w") as fp:
        json.dump(all_books, fp, indent=4)
    print(f'{user_name} returned {book_name} successfully\n')
