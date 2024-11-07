# simple calculator program

print("Welcome to Calculator")

print("Select an operation and enter numbers:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Divide")
val = int(input("Enter option number : "))

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
if val == 1:
    print(n1, " +", n2, " =", n1 + n2)
elif val == 2:
    print(n1, " -", n2, " =", n1 - n2)
elif val == 3:
    print(n1, " *", n2, " =", n1 * n2)
elif val == 4:
    print(n1, " /", n2, " =", n1 / n2)

print("Thank You for using Calculator")
