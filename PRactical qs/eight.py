# File path
file_name = "example.txt"

# Writing to the file
with open(file_name, 'w') as file:
    file.write("Hello, this is a sample text file.\n")
    file.write("You can write multiple lines.\n")
    file.write("Python makes file handling easy!\n")
print("Data written to file successfully.\n")

# Reading from the file
print("Reading data from file:")
with open(file_name, 'r') as file:
    content = file.read()
    print(content)
