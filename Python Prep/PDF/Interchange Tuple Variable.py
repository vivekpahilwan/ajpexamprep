tup1 = tuple(int(i) for i in input("Enter First tuple").split())
tup2 = tuple(int(i) for i in input("Enter Second Tuple").split())

# tup1 = tuple(input("Enter the first tuple: ")) 
# tup2 = tuple(input("Enter the second tuple: "))

print("1st", tup1)
print("2nd", tup2)

tup1, tup2 = tup2, tup1

print("1nd", tup1)
print("2nd", tup2)