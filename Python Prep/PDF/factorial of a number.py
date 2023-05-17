# num = int(input("enter the 
# fact = 1
# if num == 0:
#     print("Fact is 0")
# if num < 0:
#     print("NOt for -ve num")
# else:
#     for i in range(1, num+1):
#         fact *= i

# print(fact)

def factorial(num):
    fact = 1
    if num == 0:
        print("Zero")
    if num < 0:
        print("-ve not allowed")
    if num > 0:
        for i in range(1,num+1):
            fact *= i
    print(fact)

factorial(3)