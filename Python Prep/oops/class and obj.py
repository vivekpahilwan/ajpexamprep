class person:
    # Special method to intitalize objects in class
    # invoked when object of class is created
    # Main purpose is to intitalize values
    # It always returns none

    # TYPES
    # Parameterized Constructor = when it accepts args along with self keyword
    # Default Constructor = It dosent take any arg but only has self arg

    def __init__(self, n, o):
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = person("vivek","developer")
b = person("krish","Tester")
a.info()
b.info()
