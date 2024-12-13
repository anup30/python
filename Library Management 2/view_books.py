def view_all_books(all_books):
    if len(all_books) > 0:
        print('The book list is :')
        for i in range(0, len(all_books)):
            print(i+1, end=". ")
            print(
                f"Title: {all_books[i]['title']} | Author: {all_books[i]['author']} | isbn: {all_books[i]['isbn']} "
                f"| Year: {all_books[i]['year']} | Price: {round(all_books[i]['price'], 2)} " 
                f"| In Stock : {all_books[i]['quantity']} | Borrowed : {all_books[i]["borrowed"]} "
                f"| Book Entry time: {all_books[i]['add_time']} | Last Update time: {all_books[i]['update_time']}")
        print()
    else:
        print("Book List is Empty.\n")
