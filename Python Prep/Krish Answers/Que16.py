d1 = {"0":"Zero", "1":"One", "2":"Two", "3":"Three", "4":"Four"}
num = input("Enter a number:")
l1 = []
for item in num:
    l1.append(d1[item])
print(" ".join(l1))
