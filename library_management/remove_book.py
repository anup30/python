# remove a book data from database
import view_books
import csv
properties = ["title", "author", "isbn", "year", "price", "quantity"]


def remove_it(books):
    if len(books) < 2:
        print("Book list is empty so you cant remove any. add some book(s) first")
    else:
        print("The Book list is : ")
        view_books.show_books(books)
        select = int(input("Select the number from the above list, which you want to delete : "))
        if 1 <= select <= len(books):
            # remove at index:
            books.pop(select)
            # remove from database:
            with open("all_books.csv", mode="w", newline='') as write_file:
                csv_writer = csv.writer(write_file)
                csv_writer.writerow(properties)
                for i in range(1, len(books)):
                    csv_writer.writerow(books[i])

            print(f"Book {select} removed from database!\n")
        else:
            print("invalid choice, try again.\n")
