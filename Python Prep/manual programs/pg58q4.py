# Define the sample data list
sample_data = [{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]

# Create a set to store unique values
unique_values = set()

# Iterate through each dictionary in the list
for d in sample_data:
    # Iterate through each key-value pair in the dictionary
    for key, value in d.items():
        # If the value is not already in the set, add it
        if value not in unique_values:
            unique_values.add(value)

# Print the unique values
print("Unique values:")
for value in unique_values:
    print(value)
