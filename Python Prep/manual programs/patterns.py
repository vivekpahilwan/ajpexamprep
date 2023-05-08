for i in range(4):
    for j in range(i+1):
        print("*", end=" ")
    print("\r")


print("\n")

for i in range(4):
    # for printing spaces
    for j in range(4-i-1):
        print(" ", end="")
        
	#for printing stars
    for j in range (i+1):
        print("*",end=" ")
    print("\r")
    

for i in range(4):
    for j in range(i+1):
        print("+", end="")
    print("\r")
