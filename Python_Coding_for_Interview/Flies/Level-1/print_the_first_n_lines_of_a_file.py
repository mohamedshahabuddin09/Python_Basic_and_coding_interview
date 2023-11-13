file_path="basic_file.txt"

n=int(input("How many lines would you like to read"))

with open(file_path) as file:
    lines=file.readlines()
    print(lines)
    num_lines=len(lines)

    if num_lines<n:
        print("enter valif file number")

    else:
        for i in range(n):
            print(lines[i].strip("\n"))