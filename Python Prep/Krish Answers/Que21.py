str = input("Enter a string: ")
uc = 0
lc = 0
for i in str:
    if i.isupper():
        uc += 1
    elif i.islower():
        lc += 1
print(uc)
print(lc)
