# Subtraction
def subtraction(x, y):
    z = x - y
    return z


# Addition
def addition(x, y):
    z = x + y
    return z


# Multiplication
def multiply(x, y):
    z = x * y
    return z


# Division
def divide(x, y):
    try:
        out = x / y
        return out
    except ZeroDivisionError:
        print("Division By 0 Error")
        return 0


first = float(input("1st Number: "))
second = float(input("2nd Number: "))
operation = input("Operation (+,-,*,\\): ")

if operation == "+":
    print(addition(first, second))
elif operation == "-":
    print(subtraction(first, second))
elif operation == "*":
    print(multiply(first, second))
elif operation == "\\":
    print(divide(first, second))
else:
    print("Invalid Opeartion")

