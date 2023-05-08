num = int(input("Enter the number you want the factorial of"))

factorial = 1

for i in range(1 , num +1):
    factorial *= i

print(factorial)