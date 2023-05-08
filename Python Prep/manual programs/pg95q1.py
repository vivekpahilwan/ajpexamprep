class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def read_employee_info(self):
        self.name = input("Enter employee name: ")
        self.department = input("Enter department: ")
        self.salary = float(input("Enter salary: "))

    def print_employee_info(self):
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)


# Example usage
emp = Employee("John Doe", "Sales", 50000.0)
emp.print_employee_info()
emp.read_employee_info()
emp.print_employee_info()
