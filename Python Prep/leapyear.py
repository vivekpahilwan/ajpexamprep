year = int (input("Enter year"))
if (year % 400 == 0 or year % 100 != 0 and year % 4 == 0):
        print("Leap")
else:
        print("Not Leap")


