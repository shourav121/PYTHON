# Creating a dictionary
my_dict = {
    "name": "gaurav",
    "age": 19,
    "city": "ambala",
    "job": "student"
}

# 1. Display the original dictionary
print("Original Dictionary:", my_dict)

# 2. Accessing a value using a key
print("Value for key 'name':", my_dict["name"])

# 3. Adding a new key-value pair
my_dict["salary"] = 50000
print("After adding 'salary':", my_dict)

# 4. Updating an existing key-value pair
my_dict["age"] = 26
print("After updating 'age':", my_dict)

# 5. Removing an element using `del`
del my_dict["city"]
print("After deleting 'city':", my_dict)

# 6. Removing an element using `pop`
job = my_dict.pop("job")
print(f"After popping 'job' ({job}):", my_dict)

# 7. Getting a value using `get()` (avoiding KeyError)
print("Using get() for 'name':", my_dict.get("name"))
print("Using get() for 'address' (not present):", my_dict.get("address", "Not Found"))

# 8. Checking if a key exists
print("Is 'age' in dictionary?", "age" in my_dict)

# 9. Getting all keys
print("All Keys:", list(my_dict.keys()))

# 10. Getting all values
print("All Values:", list(my_dict.values()))

# 11. Getting all key-value pairs
print("All Key-Value Pairs:", list(my_dict.items()))

# 12. Iterating over dictionary keys
print("Iterating over keys:")
for key in my_dict:
    print(key, "->", my_dict[key])

# 13. Copying a dictionary
copied_dict = my_dict.copy()
print("Copied Dictionary:", copied_dict)

# 14. Clearing the dictionary
my_dict.clear()
print("After clearing the dictionary:", my_dict)
