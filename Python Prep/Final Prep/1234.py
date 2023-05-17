d1 = {"0":"Zero", "1":"One", "2":"Two", "3":"Three", "4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Nine"}
num = input("Enter a number:") # string input 
l1 = []
for char in num:
    l1.append(d1[char])
print(" ".join(l1))
print(l1)

