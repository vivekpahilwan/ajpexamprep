l = [int(a) for a in  input("Enter the items in list").split()]
print(l)

max = l[0]
for i in l:
    if i > max:
        max = i
print(max) 