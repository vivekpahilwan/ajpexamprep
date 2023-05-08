# Default argument Example
# Functions assume a default value even if a value is not provided in a function call for that arguement
# You can also give a single argument //// the other will be taken from the default one
def average(a, b=20):
    print((a+b)/2)


average(100, 2050)
average(100)

# Keyword arguement example
# We can provide argument with key value pair , in this way the interpreter recognises argument by its name
#  the order wont matter
average(b=20, a=50)

# Required arguements
average(a=1, b=45)

# def average(a, b=20):          here a is compulsory and b is optional
#     print((a+b)/2)


# Variable length argument
def manyavg(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    print("average of manu numbers is", sum/len(numbers))


manyavg(1, 2, 3, 4, 5, 6, 7,99,1000)
