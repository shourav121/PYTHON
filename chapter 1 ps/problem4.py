import os

# Specify the directory path
path = '/Log'

# Get the list of all files and directories
dir_list = os.listdir(path)

print(f"Contents of '{path}':")
for item in dir_list:
    print(item)
