# define the sample dictionary
sample_dict = {'key1': 'value1', 'key2': 'value2'}

# define the other dictionaries
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

# concatenate the dictionaries to create a new one
new_dict = {**sample_dict, **dic1, **dic2, **dic3}

# print the new dictionary
print("The concatenated dictionary is:", new_dict)
