def divide(x, y):
    try:
        out = x / y
        return out
    except ZeroDivisionError:
        print("Division By 0 Error")
        return 0
