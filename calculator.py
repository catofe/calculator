# Multiplication 
def multiply(x, y):
    z = x * y
    return z

# division function
def divide(x, y):
    try:
        out = x / y
        return out
    except ZeroDivisionError:
        print("Division By 0 Error")
        return 0
