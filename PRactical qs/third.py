import math

def area_circle():
    radius = float(input("Enter the radius of the circle: "))
    return math.pi * radius ** 2

def area_rectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    return length * width

def area_triangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    return 0.5 * base * height

def area_square():
    side = float(input("Enter the side length of the square: "))
    return side ** 2

# Menu-driven program using a while loop
while True:
    print("\nMenu: Calculate Area")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Square")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        print(f"Area of Circle: {area_circle():.2f}")
    elif choice == '2':
        print(f"Area of Rectangle: {area_rectangle():.2f}")
    elif choice == '3':
        print(f"Area of Triangle: {area_triangle():.2f}")
    elif choice == '4':
        print(f"Area of Square: {area_square():.2f}")
    elif choice == '5':
        print("Exiting the program. Thank you!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")

