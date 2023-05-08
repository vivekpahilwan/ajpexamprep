class Employee:
    def __init__(self, i, n):
        self.id = i
        self.name = n

    def display(self):
        print(f"ID:{self.id}\nName:{self.name}")


e1 = Employee(206, "vivek")
e1.display()
