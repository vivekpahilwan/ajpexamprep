t = ()
l = []
s = {}
print(type(t))
print(type(l))
print(type(s))

my_dict = {1: "John", 2: "Vivek", 3: "New York"}
# print(my_dict.values())
print(my_dict.items())
# print(my_dict.pop("age"))
print(all(my_dict))
print("*****************")


x = 18  # Global variable


def my_function():

    global x  # Indicate that we're referring to the global variable
    x = 20   # Modifying the global variable
    print(x)

    y = 90  # Local Variable
    print(y)


my_function()  # Output: 20
print(x)  # Output: 20

print("*****************Elif Ladder****************")

age = 0
if (age > 18):
    print("allowed")
elif (age < 18):
    print("Not allowed")
elif (age == 0):
    print("Invalid age")
else:
    print("No Entry")