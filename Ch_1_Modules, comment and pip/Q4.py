import os

# Specify the path (you can use '.' for the current directory)
path = '/JAVA'

# Get the list of all files and directories
try:
    contents = os.listdir(path)
    print("Contents of the directory:")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The specified directory was not found.")
except PermissionError:
    print("You do not have permission to access this directory.")
