d = {"0": "Zero", "1": "One", "2": "Two", "3": "Three", "4": "Four",
     "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine"}
num = input("Enter a number:")  # string input
res = ''

for i in num:
    res = res + " " + d.get(i)

print(res)
