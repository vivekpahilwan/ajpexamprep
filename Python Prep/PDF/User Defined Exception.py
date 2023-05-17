class AgedError(Exception):
    pass


try:
    age = int(input("ENter Age"))
    if age < 18:
        raise AgedError
    else:
        print("Welcomw to voting")
except AgedError:
    print("Age small")
