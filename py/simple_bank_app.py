# project: simple Bank app
print("Welcome to Bank App")


class Bank:
    name = ""
    __balance = None  # private variable

    @property
    def balance(self):  # getter
        return self.__balance

    @balance.setter
    def balance(self, new_balance):  # setter
        self.__balance = new_balance

    def __init__(self, account_name, initial_balance=0):
        self.name = account_name
        if initial_balance > 0:
            self.balance = initial_balance  # uses setter
        else:
            self.balance = 0  # uses setter

        print("Congratulations!")
        print(f"Account Created with name {self.name}, initial balance {self.__balance} taka")

    def account_info(self):
        print(f"Account name : {self.name}")
        print(f"Account balance : {self.__balance} taka")
        # more info can be added

    def deposit(self, amount):  # static method
        if amount > 0:
            # self.__balance += amount  # direct access
            self.balance += amount  # uses setter
            print(f"{amount} taka added to your Account, current balance is {self.balance} taka")
        else:
            print("Invalid amount")

    def withdraw_money(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} tk Withdrawn from your Account, current balance = {self.__balance}")


print("In order to create an account input your name and initial deposit(/balance)")
name = input("Your Name : ")
pre = int(input("Your Initial Deposit (taka): "))
obj = Bank(name, pre)

select = None


def print_info():
    print("Select an option below :")
    print("0. Quit App")
    print("1. Check you Account info")
    print("2. Check you Account balance")
    print("3. Deposit money to your Account")
    print("4. Withdraw Money")


def take_input():
    global select
    while True:
        print_info()
        select = input("Your Choice : ")
        if select == "0":
            print("Thank You for using our Bank App")
            break
        elif select == "1":
            obj.account_info()
        elif select == "2":
            print("Your Balance = ", obj.balance, "taka")
        elif select == "3":
            amount = int(input("Enter the amount you want to deposit : "))
            obj.deposit(amount)
        elif select == "4":
            amount = int(input("Enter the amount you want to Withdraw : "))
            obj.withdraw_money(amount)


take_input()
