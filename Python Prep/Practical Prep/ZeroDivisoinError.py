try:
    a = 5
    b = 0
    c = a / b
    print(c)
    
except (ZeroDivisionError):
    print("Dont Divide by 0")
