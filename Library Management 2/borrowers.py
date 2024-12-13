
def show_borrowers_list(all_borrowers):
    if len(all_borrowers) > 0:
        print("The borrowers list: ")
        for i in range(0, len(all_borrowers)):
            print(f"{i+1}. {all_borrowers[i]}")
        print()
    else:
        print("Borrowers List is Empty\n")
