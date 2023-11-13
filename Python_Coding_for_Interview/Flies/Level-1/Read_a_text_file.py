# Write a python program that reads a text file and saves its content line by line to a list called file_content
# The list should contain strings that represent each line of the text file
# Hint: Use with open statement

file_path="basic_file.txt"

file_content=[]

with open(file_path) as file:
    for i in file:
        file_content.append(i)
print(file_content)
