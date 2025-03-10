
import math

# Displaying some math module functions

# 1. Square root
num = 16
print(f"Square root of {num} is:", math.sqrt(num))

# 2. Power function (x^y)
x, y = 2, 3
print(f"{x} raised to the power {y} is:", math.pow(x, y))

# 3. Factorial
num = 5
print(f"Factorial of {num} is:", math.factorial(num))

# 4. Greatest Common Divisor (GCD)
a, b = 36, 60
print(f"GCD of {a} and {b} is:", math.gcd(a, b))

# 5. Trigonometric Functions
angle = math.radians(30)  # Convert degrees to radians
print(f"Sine of 30 degrees:", math.sin(angle))
print(f"Cosine of 30 degrees:", math.cos(angle))
print(f"Tangent of 30 degrees:", math.tan(angle))

# 6. Logarithmic Functions
num = 100
print(f"Natural log of {num} is:", math.log(num))  # Natural log (base e)
print(f"Log base 10 of {num} is:", math.log10(num))

# 7. Constants
print("Value of π (pi):", math.pi)
print("Value of e (Euler's number):", math.e)
