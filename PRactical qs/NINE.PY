# Base class
class Person:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"Name: {self.name}")

# Derived class using Inheritance
class Employee(Person):
    def __init__(self, name, salary=0):
        super().__init__(name)
        self.salary = salary

    # Function Overloading (using default argument)
    def show_info(self, show_salary=True):
        print(f"Name: {self.name}")
        if show_salary:
            print(f"Salary: {self.salary}")

    # Operator Overloading: Add salaries of two employees
    def __add__(self, other):
        if isinstance(other, Employee):
            return self.salary + other.salary
        return NotImplemented

# Creating objects
emp1 = Employee("GAURAV", 5000)
emp2 = Employee("VIKASH", 7000)

print("=== Employee 1 Info ===")
emp1.show_info()

print("\n=== Employee 2 Info ===")
emp2.show_info(show_salary=False)  # Function overloading via argument

# Operator Overloading Demo
total_salary = emp1 + emp2
print(f"\nTotal Combined Salary (emp1 + emp2): {total_salary}")
