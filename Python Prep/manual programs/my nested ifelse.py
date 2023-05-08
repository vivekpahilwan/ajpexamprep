num = int(input("Enter any number of your choice"))
if(num<0):
     print("Num is negative")

elif(num>0):
        if(num>=1 and num<=10):
            print("Number is between 1 to 10")
        elif(num>=11 and num<=20):
             print("Number is between 11 to 20")
        else:
             print("Number is Greater than 20")
else:
     print("Number is Zero")