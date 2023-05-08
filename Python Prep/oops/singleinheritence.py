class Animal:
    def feed(self):
        print("Class Animal feed method")

class Herbivorous(Animal):
    def feed(self):
        print("Class Herbivorous feed method")

obj = Herbivorous()
obj.feed()