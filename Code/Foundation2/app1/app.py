import os

# Get Current Working Dir
print(f'CWD: {os.getcwd()}')

# Change Dir
os.chdir("Z:\Git\Pythonic\Code")
print(f'CWD: {os.getcwd()}')

os.chdir("Z:\Git\Pythonic\Code\Foundation2")
print(f'CWD: {os.getcwd()}')

# List Dir
print(os.listdir())

# Make Dir
if "Temp" not in os.listdir():
    os.mkdir("Temp")
    print(os.listdir())

# Make Sub-Folders
if "Temp" not in os.listdir():
    os.makedirs("Temp\Gen1\Gen2\Gen3")

# Remove a file
if "log1.txt" in os.listdir():
    os.remove("Temp\Gen1\Gen2\Gen3\log1.txt")

# Remove a particular folder, i.e. Gen3
# NOTE: The folder must be empty
# os.rmdir("Temp\Gen1\Gen2\Gen3")

# NOTE: WARNING!!! Removes the parent and sub-folder
# os.removedirs("Temp\Gen1")

# Rename file
os.rename("Temp\log2.txt", "Temp\log3.txt")