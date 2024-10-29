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