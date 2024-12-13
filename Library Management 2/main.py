# Library Management App 2
import add_book
import borrow_book
import borrowers
import delete_book
import load_from_file
import update_book
import view_books

import return_book

print("\nWelcome to Library Management System App")
all_books = load_from_file.load_all_books()
all_borrowers = load_from_file.load_all_borrowers()


def print_info():
    print("Please Select an option from below :")
    print("1. View All Books Data")
    print("2. Add a Book Data")
    print("3. Update a Book Data")
    print("4. Delete a Book Data")
    print("5. Borrow a Book")
    print("6. Return borrowed book")
    print("7. See Borrowers list")
    print("0. Exit App")
    print()


while True:
    print_info()
    choice = input("Select any number: ")

    if choice == "1":
        view_books.view_all_books(all_books)

    elif choice == "2":
        all_books = add_book.add_to_database(all_books)

    elif choice == "3":
        update_book.update_books(all_books)

    elif choice == "4":
        all_books = delete_book.delete_books(all_books)

    elif choice == "5":
        borrow_book.borrow_a_book(all_books, all_borrowers)

    elif choice == "6":
        return_book.return_book(all_books, all_borrowers)

    elif choice == "7":
        borrowers.show_borrowers_list(all_borrowers)

    elif choice == "0":
        print("Thank You for using Library Management System App\n")
        break

    else:
        print("Invalid choice, please try again")
