class A:
    pass


class B:
    pass


class C(B, A):
    pass

print(C.mro())
# mro() is a method resolution order which tells that which overriden method will be called first
# genrally its the latest child class method
