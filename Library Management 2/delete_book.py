import save_book_list


def delete_books(all_books):
    search_book = input("Enter Book Title to Delete: ")
    for book in all_books:
        if book["title"] == search_book:
            if book['borrowed'] > 0:
                print("Book data cannot be deleted, when some one has borrowed copy.")
                print("all borrowed books have to be returned first to delete.\n")
                return
            all_books.remove(book)
            save_book_list.save_all_books(all_books)
            print("Book Deleted Successfully\n")

    print("Book Not Found\n")
