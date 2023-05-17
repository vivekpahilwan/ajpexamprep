# Creating a parent class named Animals
class Animals:
    def feed(self):
        print("This is A parent class method feed ()")

# Creating a Child class named Herbivorous


class Herbivorous(Animals):
    def feed(self):
        print("This is a Child class method feed ()")
    # def feed(self):
    #     return super().feed()


# Creating an Object of child class Herbivorous
obj = Herbivorous()

# Calling a function of  Child class
obj.feed()
