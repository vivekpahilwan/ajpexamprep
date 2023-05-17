l = list(int(i) for i in input("Enter the items in list").split())

print(sum(l))

sum = 0
for item in l:
    sum += item

print(sum)
