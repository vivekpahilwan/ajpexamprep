# Every input is a String in  python
a = input("Enter 1st number: ")
b = input("Enter 2nd number: ")
print("Without Typecasting", a+b)
print("with Typecasting", int(a)+int(b))

x = "Vivek"
s = type(print("Hello", x))
e = type(print("Hello" + x))
print(s)
print(e)