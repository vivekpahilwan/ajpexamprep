with open('\\demofile.txt') as f1:
    contents = f1.read()

with open('\\demofile2.txt') as f2:
    f2.write(contents)