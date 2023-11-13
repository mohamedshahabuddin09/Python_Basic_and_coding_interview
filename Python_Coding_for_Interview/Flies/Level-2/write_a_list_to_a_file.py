
list=[1,3,4,5]

with open("list_write","w") as file:
        for elem in list:
            file.write(str(elem)+ "\n")