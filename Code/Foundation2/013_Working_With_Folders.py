import os

for path, folders, files in os.walk("Temp\Sub1"):
    print(f'Path: {path}')
    print(f'Folders: {folders}')
    print(f'Files: {files}')

    print()