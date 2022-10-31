
def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y

"""x = input("Enter first operand:")
y = input("Enter second operand:")

print("Calculator Menu")
print("---------------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")"""

while True:
    x = input("Enter first operand:")
    y = input("Enter second operand:")

    print("Calculator Menu")
    print("---------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Which operation do you want to perform:")

    if choice in ('1','2','3','4'):
        num1 = float(x)
        num2 = float(y)

    if choice == '1':
        print("The result of the operation is",(add(num1,num2)))
    elif choice == '2':
        print(subtract(num1,num2))
    elif choice == '3':
        print(multiply(num1, num2))

    elif choice == '4':
        print(divide(num1, num2))

    else:
        print("Error:Invalid selection! Termanting program.")
            


