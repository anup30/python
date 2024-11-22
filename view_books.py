def show_books(books):
    if len(books) < 2:
        print("list is empty, try adding some\n")
    else:
        for i in range(0, len(books)):
            if i == 0:
                print("  ", books[0])
            else:
                print(f"{i})", books[i])
        print()
