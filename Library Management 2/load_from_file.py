import json
import os


def load_all_books():
    if not os.path.exists("all_books.json"):
        print("all_books.json file not found! create some books database.")
        return []
    with open("all_books.json", "r") as fp:
        book_list = json.load(fp)
        # book_list.sort(key=lambda x: (x['title'], x['author'], x['isbn']))  # keep sorted
    return book_list


def load_all_borrowers():
    if not os.path.exists("all_borrowers.json"):
        print("all_borrowers.json file not found! create some borrowers database.")
        return []
    with open("all_borrowers.json", "r") as fp2:
        borrower_list = json.load(fp2)
        # borrower_list.sort(key=lambda x: (x['name'], x['phone']))  # keep sorted
    return borrower_list

