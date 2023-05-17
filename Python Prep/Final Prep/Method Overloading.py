# method overloading is a concept of defining multiple methods with same name and different paremeters
# A method can perform differnt  tasks based on the number of arguments given to the method
# Method overloading is not possible in python because the type of argument which is to be passed is not known
# argument can be of diffent type  like int string float
# the newly defined method will be considered as valid

# First product method.
# Takes two argument and print their
# product


def product(a, b):
    p = a * b
    print(p)


def product(a, b, c):
    p = a * b*c
    print(p)


product(4, 5)

class abc:
    def methodofclass(self, arg):
        print(a)