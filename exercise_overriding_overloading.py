class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):  # Inherits from B and C
    pass

d = D()
print("\nMRO Example:")
d.show()  # Will print "Class B" due to MRO
print(D.__mro__)  # Prints the method resolution order
