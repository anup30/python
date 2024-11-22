# edit a book info in database
import view_books
import csv

properties = ["title", "author", "isbn", "year", "price", "quantity"]
book = {
    'title': 'title',
    'author': 'author',
    'isbn': 123,
    'year': 123,
    'price': 0.50,
    'quantity': 1,
}
new_book = []


def input_book():
    book["title"] = input("Enter Book Title (string): ")
    book["author"] = input("Enter Author(s) (string): ")
    book["isbn"] = int(input("Enter ISBN (number): "))
    book["year"] = int(input("Enter Publishing Year (number): "))  # to update: implement try except
    book["price"] = float(input("Enter Book Price (float): "))
    book["quantity"] = int(input("Enter Quantity (number): "))


def edit_it(books):
    if len(books) < 2:
        print("Book list is empty so you cant edit any. add some book(s) first")
    else:
        print("The Book list is : ")
        view_books.show_books(books)
        select = int(input("Select the number from the above list, which you want to edit : "))
        if 1 <= select <= len(books):
            input_book()
            for value in book.values():
                new_book.append(value)
            books[select] = new_book
            with open("all_books.csv", mode="w", newline='') as write_file:
                csv_writer = csv.writer(write_file)
                csv_writer.writerow(properties)
                for i in range(1, len(books)):
                    csv_writer.writerow(books[i])

            print(f"Book {select} edited in database!\n")
        else:
            print("invalid choice, try again.\n")
