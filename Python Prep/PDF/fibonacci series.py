a, b = 0, 1
till = int(input("Enter num till which you want series"))

for i in range(0, till):
    print(b)
    new = a+b
    a, b = b, new
