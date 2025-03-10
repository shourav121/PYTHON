
# Creating a list
my_list = [10, 20, 30, 40, 50]

# 1. Display the original list
print("Original List:", my_list)

# 2. Append an element to the list
my_list.append(60)
print("After appending 60:", my_list)

# 3. Insert an element at a specific index
my_list.insert(2, 25)  # Insert 25 at index 2
print("After inserting 25 at index 2:", my_list)

my_list.remove(40)  
print("After removing 40:", my_list)


popped_element = my_list.pop()
print(f"After poppping  ({popped_element}):", my_list)

popped_element = my_list.pop(2)
print(f"After popping element at index 2 ({popped_element}):", my_list)

index = my_list.index(30)
print("Index of 30:", index)


count = my_list.count(20)
print("Occurrences of 20:", count)

# 9. Reverse the list
my_list.reverse()
print("After reversing the list:", my_list)

# 10. Sort the list in ascending order
my_list.sort()
print("After sorting in ascending order:", my_list)

# 11. Sorting in descending order
my_list.sort(reverse=True)
print("After sorting in descending order:", my_list)

# 12. Copy the list
copied_list = my_list.copy()
print("Copied List:", copied_list)

# 13. Extend the list with another list
my_list.extend([70, 80, 90])
print("After extending with [70, 80, 90]:", my_list)

# 14. Slicing the list
sliced_list = my_list[1:4]  # Elements from index 1 to 3
print("Sliced List (index 1 to 3):", sliced_list)

# 15. Clearing the list
my_list.clear()
print("After clearing the list:", my_list)
