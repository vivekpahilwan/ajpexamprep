till = int(input("Enter the number till which you want the fibonacci series"))

a, b = 1, 2

for i in range(0, till):
    print(b)
    new = a+b
    a, b = b, new
