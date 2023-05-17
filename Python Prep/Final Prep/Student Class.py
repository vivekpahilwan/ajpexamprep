class student:

    def read_details(self, name, roll, address):
         self.name = name
         self.roll = roll
         self.address = address

    def show_details(self):    
        print("name",self.name)
        print("roll",self.roll)
        print("address",self.address)

obj = student()

obj.read_details("vivek",206,"Main Road")
obj.show_details()