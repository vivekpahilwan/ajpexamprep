# num = str(input("Enter a number"))
# x=[i for i in num]
# print(type(x))
# num = list(int(i) for i in input("Enter numbers").split())
# print(num)

num = input("Enter Number: ")
sum = 0

for i in num:
    sum = sum + int(i)

print(sum)
