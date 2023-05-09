# def find_repeated_items(my_tuple):
#     repeated_items = []

#     # Iterate through each item in the tuple
#     for item in my_tuple:
#         # Check if the count of the item is greater than 1
#         if my_tuple.count(item) > 1:
#             # Append the item to the repeated_items list if it's not already present
#             if item not in repeated_items:
#                 repeated_items.append(item)

#     return repeated_items

# tup =(1,2,4,5,6,7,2,22,2,3,3,1,9)
# print(find_repeated_items(tup))


tup = (1, 2, 2,2,1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# create a list to store Repeated items
repeated_items = []
# use count function
# repeat for every item using loop
for i in tup:
    if tup.count(i) > 1 and i not in repeated_items:
            repeated_items.append(i)
print(repeated_items)
