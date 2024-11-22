# load books info from database/all_books.csv file
import os
import csv
import view_books


def load_from_database(books, view=False):
    if os.path.exists("all_books.csv"):
        with open("all_books.csv", "r") as read_file:  # check if file exists
            content = csv.reader(read_file)
            books.clear()
            for row in content:
                books.append(row)
        if view:
            view_books.show_books(books)

    else:
        print("all_books.csv file not found! try adding some book(s)\n")

