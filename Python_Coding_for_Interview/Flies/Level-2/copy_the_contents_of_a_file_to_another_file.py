file_path="famous.txt"
copy_path="famous_2.txt"

with open(file_path) as file,open(copy_path,"w") as copy_file:
    for elem in file:
        copy_file.write(elem)