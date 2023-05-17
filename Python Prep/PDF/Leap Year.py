y = int(input("Enter Year"))
if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
    print(y,"IS a Leap Year")
else:
    print("Not a leap")
