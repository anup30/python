# Project: Favourite Food Manager app

print("Welcome to Favourite Food Manager app")

favourite_foods = []
multi_line = """
Make a Choice: 
0. Quit app    
1. Add a food to Favourites list
2. Remove a food from Favourites list
3. Show all foods from Favourites list
"""
print(multi_line)
while True:
    choice = input("Enter Number : ")
    if choice == "0":
        print("Thank you for using Favourite Food Manager app")
        break

    elif choice == "1":
        food = input("Enter a food Name to Add : ")
        favourite_foods.append(food)
        print(f"{food} has been added to Favourite Food list")

    elif choice == "2":
        if len(favourite_foods) == 0:
            print("Favourite Food list is empty, no items to remove")
        else:
            food = input("Enter a food Name to Remove : ")
            if food in favourite_foods:
                favourite_foods.remove(food)  # removes the first occurrence
                print(f"{food} has been removed from Favourite Food list")
            else:
                print(f"{food} is not present in Favourite Food list, check spelling and try again")

    elif choice == "3":
        if len(favourite_foods) == 0:
            print("Favourite Food list is currently empty")
        else:
            print("The following foods are present in the Favourite Food list: ")
            for index, element in enumerate(favourite_foods, start=1):
                print(f"{index}. {element}")

    else:
        print("Invalid Choice")
    print(multi_line)
