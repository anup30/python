import save_book_list
from datetime import datetime


def update_books(all_books):
    search_book = input("Enter Book Title to Update: ")
    found = False
    for book in all_books:
        if book["title"].lower() == search_book.lower():
            if book['borrowed'] > 0:
                print("Book data cannot be updated, when some one has borrowed copy.")
                print("all borrowed books have to be returned first to update.\n")
                return
            found = True
            while True:
                try:
                    title = input("Enter Book Title: ")
                    author = input("Enter Author Name: ")
                    year = int(input("Enter Publishing Year Number: "))
                    price = float(input("Enter Book Price: "))
                    quantity = int(input("Enter Quantity Number: "))
                    break
                except Exception as e:
                    print("error :", e, 'try again')

            book_last_updated_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            book["title"] = title
            book["author"] = author
            book["year"] = year
            book["price"] = price
            book["quantity"] = quantity
            book["update_time"] = book_last_updated_at

            save_book_list.save_all_books(all_books)
            print("Book Updated Successfully\n")

    if not found:
        print("Book Not Found in Database!\n")
