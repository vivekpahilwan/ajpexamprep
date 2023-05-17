class Employee:

    def readinfo(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print(self.name)
        print(self.department)
        print(self.salary)


obj = Employee(None)
obj.readinfo("vivek", "Comp", 50000)
obj.display()
