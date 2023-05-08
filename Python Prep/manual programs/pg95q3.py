class A:
    def method_a(self):
        print("This is method A")


class B:
    def method_b(self):
        print("This is method B")


class C(A, B):
    def method_c(self):
        print("This is method C")


# Example usage
x = C()
x.method_a()
x.method_b()
x.method_c()
