

# assume content is already present in file 1
f1 = open('file1.txt', 'r')
contents = f1.read()

f2 = open('file2.txt', 'w')
f2.write(contents)
