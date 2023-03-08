num = int(input('Enter a number of your choice: '))

match num:
    case 1:
        print("Number is 1")
    case 10:
        print("Number is 0")
    case _ if (num != 90):     # default cases are written as underscore
        print("NUm is not equal to 90")
    case 90:
        print("Number is 90")

