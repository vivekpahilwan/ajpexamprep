list = [1, 2, 54, 543, 23, 4]

# using max function
print("By using max function", max(list))

# using loop
# assume 1st element in List is largest
largest = list[0]
for num in list:
    if num > largest:
        largest = num
print("By using for loop and if statement: ", largest)
