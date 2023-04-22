# define a dictionary
my_dict = {'apple': 20, 'banana': 10, 'cherry': 30, 'dates': 5}

# sort the dictionary by value in ascending order
sorted_dict_ascending = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}

# sort the dictionary by value in descending order
sorted_dict_descending = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1], reverse=True)}

# print the sorted dictionaries
print("Dictionary sorted by value in ascending order:", sorted_dict_ascending)
print("Dictionary sorted by value in descending order:", sorted_dict_descending)
