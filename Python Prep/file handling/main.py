# # Open abc.txt file in read mode
# f = open('D:\\repos\\Exam Prep\\Python Prep\\file handling\\demofile.txt', 'r')
#     # Read the contents of the file
# contents = f.read()

# # Open pqr.txt file in write mode
# f = open('D:\\repos\\Exam Prep\\Python Prep\\file handling\\demofile2.txt', 'w')
#     # Write the contents to the new file
# f.write(contents)

# print(type(contents))


f = open('D:\\repos\\Exam Prep\\Python Prep\\file handling\\demofile.txt', 'w')
lines = "This is some contents in file 1"
f.write(lines)
f.close()

f = open('D:\\repos\\Exam Prep\\Python Prep\\file handling\\demofile.txt', 'a')
appended_content = "contents appended"
appended_list = ["\none", "\ntwo", "\nthree",]
f.writelines(appended_list)
