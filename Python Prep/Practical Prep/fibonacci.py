till = int(input("Enter the number till which you want the fibonacci series"))

# initialize the starting value for starting
a, b = 0, 1

for i in range(0, till):
    print(b)
    new = a+b
    a, b = b, new

#             a <-- b         b <-- new 
# print b
# put value of 2nd no  into 1st no
# put value of new into 2nd
# and put value of new into b
