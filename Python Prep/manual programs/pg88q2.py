class Animal:
 # properties
    multicellular = True
# Eukaryotic means Cells with Nucleus
    eukaryotic = True
# function breath

    def breathe(self):
        print("I breathe oxygen.")
 # function feed

    def feed(self):
        print("I eat food.")
 # child class


class Herbivorous(Animal):
 # function feed
    def feed(self):
        print("I eat only plants. I am vegetarian.")


herbi = Herbivorous()
herbi.feed()
# calling some other function
herbi.breathe()
