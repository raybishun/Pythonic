import os

# Traverse folders
for path, folders, files in os.walk("Temp\Sub1"):
    # print(f'Path: {path}')
    # print(f'Folders: {folders}')
    # print(f'Files: {files}')
    # print()
    pass

# Get environment variables
print(os.environ.get("HOMEPATH"))
print(os.path.join(os.environ.get("HOMEPATH"), "Documents"))

# Get filename
print(os.path.basename("C:\\Users\\ray\\Documents\\log.txt"))

# Get full directory name
print(os.path.dirname("C:\\Users\\ray\\Documents\\log.txt"))

# Get both the dir name and file name (as a tuple)
print(os.path.split("C:\\Users\\ray\\Documents\\log.txt"))

# Check if file and folder exists
print(os.path.exists("C:\\Users\\ray\\Documents\\log.txt"))

# Check if folder exists
print(os.path.isdir("C:\\Users\\ray\\Documents"))

# Check if file exists
print(os.path.isfile("C:\\Users\\ray\\Documents\\log.txt"))

# Get file extension by splitting folder and file name (as a tuple)
print(os.path.splitext("C:\\Users\\ray\\Documents\\log.txt"))