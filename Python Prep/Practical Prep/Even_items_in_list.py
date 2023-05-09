list = list(int(n) for n in input("Enter items in list: ").split())
# Printing Even Index Items
print(list[1::2])

# Printing Even elements in List
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = [i for i in list2 if i % 2 == 0]
print(even_list)
