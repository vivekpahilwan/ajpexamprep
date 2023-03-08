
# Strings are immutable

# Declaring a String
name = "!!Vivek Pahilwan Pahilwan!!!! !!!!!!!"

# Printing length of string using len() function
print("Vivek's full names is a ", len(name), "Character word")

# print(name[0:4])
# print(name[1:4])
# print(name[4])     # prints the 4th character of the string
# print(name[:4])    # starts printing from the start of the string
# print(name[:])     # prints till teh length of the string
# print(name[0:-3])  # prints till length of name - 3     (default is -1)
# print(name[0:len(name)-3])   # same as above
# print(name[-8:-1])

# Printing every character in string
for char in name:
    print(char)


# Change string to uppercase [var.upper()]
print(name.upper())

# Change string to Lowercase [var.lower()]
print(name.lower())

# strip the content [var.rstrip()]    (only strips from the end)
print(name.rstrip("!"))

# [var.replace("Old string match","new string match")]
print(name.replace("Pahilwan", "Hello"))

# var.split("reference")  =  slpits elements using the reference and adds the spiltted elements into a list
l = name.split(" ")
print("Splitted string is = ",l)

#capatilize()
heading = "introDucTion to pyThon"
print(heading.capitalize())   #capitilizes the first word of the sentence # and lowers all other characters

#center()
print(heading.center(50))
print(len(heading.center(50)))
print(len(heading))

#count()
print(name.count("Pahilwan")) #tells you how manu times did the match occur in the string