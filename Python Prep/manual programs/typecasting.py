a = 1
b = 2
print(float(a)+float(b))
print(int(a)+float(b))
print(hex(a)+hex(b))

# some functions used for typecasting
# int(), float(), hex(), oct(), str()


# implicit typecasting
x = 1     # it will convert int to float
y = 2.3   # it wont convert float to int
# python converts smaller datatype to higher datatype to prevent loss

print(type(x))
print(type(y))
print(x+y)
