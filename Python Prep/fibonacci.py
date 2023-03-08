# Fibonacci series
a, b = 0, 1
till = int(input("Enter a number till which you want the fibonacci series "))
for i in range(0, till):
    print(b)
    new = a+b
    a = b
    b = new