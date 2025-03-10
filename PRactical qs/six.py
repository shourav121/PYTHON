# Creating a tuple
my_tuple = (10, 20, 30, 40, 50)

# 1. Display the original tuple
print("Original Tuple:", my_tuple)

# 2. Access elements using indexing
print("Element at index 2:", my_tuple[2])

# 3. Slicing a tuple
print("Sliced Tuple (index 1 to 3):", my_tuple[1:4])

# 4. Concatenation of tuples
new_tuple = my_tuple + (60, 70, 80)
print("After Concatenation:", new_tuple)

# 5. Repeating a tuple
repeated_tuple = my_tuple * 2
print("After Repetition:", repeated_tuple)

# 6. Find the index of an element
index = my_tuple.index(30)
print("Index of 30:", index)

# 7. Count occurrences of an element
count = my_tuple.count(20)
print("Occurrences of 20:", count)

# 8. Length of tuple
print("Length of the tuple:", len(my_tuple))

# 9. Converting tuple to list (workaround to modify elements)
tuple_to_list = list(my_tuple)
tuple_to_list.append(60)
modified_tuple = tuple(tuple_to_list)
print("Tuple after converting to list and modifying:", modified_tuple)

# 10. Demonstrating Tuple Immutability
try:
    my_tuple[2] = 100  # Attempt to modify a tuple (not allowed)
except TypeError as e:
    print("Error! Tuples are immutable:", e)

# 11. Deleting a tuple completely (not modifying)
del my_tuple
print("Tuple deleted successfully!")

