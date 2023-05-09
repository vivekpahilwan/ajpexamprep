num = int(input("Enter a number:"))
a = 0
b = 1
if num <= 0:
    print("Enter number greater than zero")
elif num == 1:
    print("Fibbonacci serie is 0")
else:
    print("Fibbonacci series:")
    for i in range(num+1):
        print(a)
        c = a + b
        a = b
        b = c
