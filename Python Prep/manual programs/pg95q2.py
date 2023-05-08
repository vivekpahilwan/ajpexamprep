class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def read_person_info(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        
    def print_person_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Student(Person):
    def __init__(self, name, age, roll_no, marks):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.marks = marks
        
    def read_student_info(self):
        self.read_person_info()
        self.roll_no = input("Enter roll number: ")
        self.marks = float(input("Enter marks: "))
        
    def print_student_info(self):
        self.print_person_info()
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)

# Example usage
stud = Student("John Doe", 20, "CS101", 90.5)
stud.print_student_info()

stud.read_student_info()
stud.print_student_info()
