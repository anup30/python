# Library Management System app
# project for week 3

import load_books
import save_books
import remove_book
import edit_book
import view_books

print("Welcome to Library Management System app\n")
books = []


def init():
    global books
    load_books.load_from_database(books, view=False)


init()
selected = ""


def print_info():
    print("Please select an option from below : ")
    print("1. view all books info from database")  # from all_books.csv file
    print("2. add new book to database")
    print("3. edit a book info in database")
    print("4. remove a book info from database")
    print("5. close app\n")
    global selected
    selected = input("please enter a choice : ")


while True:
    print_info()
    if selected == "5":
        print("Thank You for using our Library Management System app")
        break

    elif selected == "1":
        view_books.show_books(books)  # load from csv file

    elif selected == "2":
        # print("books = ", books)
        save_books.save_it(books)  # input and save a new book data, both to database and books list

    elif selected == "3":
        edit_book.edit_it(books)

    elif selected == "4":
        remove_book.remove_it(books)

    else:
        print("invalid choice, please try again\n")
