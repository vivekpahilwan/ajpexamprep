class student:
    name = "Vivek"
    roll_no = 206
    address = "Main Road, Yeola"

    def print_details(self):
        print(f"Name of Student: {self.name}\nRoll number: {self.roll_no}\nAddress: {self.address}")

s = student()
s.print_details()