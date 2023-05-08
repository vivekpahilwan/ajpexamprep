# define the dictionaries
d1 = {'a':100, 'b':200, 'c':300}
d2 = {'a':100, 'b':200, 'd':400}

# create a new dictionary to store the combined values
combined_dict = {}

# loop through the keys in d1 and add their values to the new dictionary
for key in d1:
    if key in d2:
        combined_dict[key] = d1[key] + d2[key]
    else:
        combined_dict[key] = d1[key]

# loop through the keys in d2 that aren't in d1 and add their values to the new dictionary
for key in d2:
    if key not in d1:
        combined_dict[key] = d2[key]

# print the combined dictionary
print("The combined dictionary is:", combined_dict)
