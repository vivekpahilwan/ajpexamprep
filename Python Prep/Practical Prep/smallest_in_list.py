list = [123,324,23,4,2,1,3,43434,2,4234,0.2,0.1,2]
# usign min function
print("By using the min inbuilt function",min(list))

# using for loop and if condition
smallest = list[0]
for num in list:
    if num < smallest:
        smallest = num

print("By using the for loop and if statement",smallest)