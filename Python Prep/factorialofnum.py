# Factorial of a number

factorial = 1
num = int(input("Enter the number you want a factorial of"))

for i in range(1, num+1):
    factorial *= i
print(factorial)
