import os.path

file_path="famous.txt"

if os.path.isfile(file_path):
    print("File exists")
else:
    print("File not exists")