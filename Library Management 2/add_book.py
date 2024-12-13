import save_book_list
import random
from datetime import datetime


def add_to_database(all_books):
    title = input("Enter Book Title: ")
    while True:
        try:
            author = input("Enter Author Name: ")
            if author[0].isalpha():
                break
            else:
                raise ValueError('Author name did not start with a letter.')
        except ValueError as e:
            print("Error :", e, 'try again please')

    # isbn: auto generated
    while True:
        try:
            year = int(input("Enter Publishing Year : "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    while True:
        try:
            price = float(input("Enter Book Price: "))
            if price < 0:
                raise ValueError("Price can't be negative.")
            break
        except ValueError as e:
            print("Error :", e, 'try again')

    while True:
        try:
            quantity = int(input("Enter Stock Quantity : "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    isbn = random.randint(10000, 99999)
    book_added_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity,  # in stock
        "borrowed": 0,  # lent count
        "add_time": book_added_at,
        "update_time": None
    }

    all_books.append(book)
    # all_books.sort(key=lambda x: (x['title'], x['author'], x['isbn']))  # keep sorted
    # ^ sort using 3 parameters, if 1st parameter equal then use 2nd, so on
    save_book_list.save_all_books(all_books)

    print("Book Added Successfully\n")

    return all_books

# todo: keep the books sorted, by name or isbn
