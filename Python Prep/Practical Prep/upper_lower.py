str = input("Enter a String")

uc = 0
lc = 0

for i in str:
    if i.isupper():
        uc += 1
    elif i.islower():
        lc += 1

print(lc)
print(uc)
