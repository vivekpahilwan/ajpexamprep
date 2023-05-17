l = list(int(i) for i in input("Enter the items in list").split())
max = l[0]

for item in l:
    if item > max:
        max = item
print(max)