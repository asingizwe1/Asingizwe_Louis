# Parent class: Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        # This method will be inherited and reused/overridden by subclasses
        print(f"Name: {self.name}, Age: {self.age}")

# Subclass: Student
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call parent constructor
        self.student_id = student_id

    def display_info(self):
        # Method overriding: changes behavior of parent method
        super().display_info()
        print(f"Student ID: {self.student_id}")

# Subclass: Lecturer
class Lecturer(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")

# Subclass: Staff
class Staff(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")


# Examples
print("=== Student ===")
s = Student("Alice", 20, "S001")
s.display_info()

print("\n=== Lecturer ===")
l = Lecturer("Dr. Bob", 45, "Computer Science")
l.display_info()

print("\n=== Staff ===")
st = Staff("Carol", 35, "Finance")
st.display_info()
