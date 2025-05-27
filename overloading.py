def A(x,y,z):
    print("A", x, y, z)
def A(x,y):
    print("A_1", x, y)

class Calculator:
    # Simulated overloading using default arguments
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print("\nMethod Overloading Simulation:")
print(calc.add(5))         # 5
print(calc.add(5, 3))      # 8
print(calc.add(5, 3, 2))   # 10
