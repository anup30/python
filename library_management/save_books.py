import csv
import load_books

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


def save_it(books):
    input_book()
    if len(books) == 0:
        books.append(properties)
    new_book.clear()
    for value in book.values():
        new_book.append(value)
    # print("new book = ", new_book)
    books.append(new_book)
    # print("saving books = ", books)
    with open("all_books.csv", mode="w", newline='') as write_file:
        csv_writer = csv.writer(write_file)
        csv_writer.writerow(properties)        
        for i in range(1, len(books)):
            csv_writer.writerow(books[i])

    load_books.load_from_database(books, view=False)
    print("Book added to database!\n")

