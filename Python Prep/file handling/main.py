# Open abc.txt file in read mode
with open('D:\\repos\\Exam Prep\\Python Prep\\file handling\\demofile.txt', 'r') as f:
    # Read the contents of the file
    contents = f.read()

# Open pqr.txt file in write mode
with open('D:\\repos\\Exam Prep\\Python Prep\\file handling\\demofile2.txt', 'w') as f:
    # Write the contents to the new file
    f.write(contents)

print(type(contents))