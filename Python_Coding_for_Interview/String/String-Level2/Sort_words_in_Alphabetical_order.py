s="Hello World"
new_str=""
ss=s.split(" ")

for word in ss:
    new_str+="".join(sorted(word.lower()))+" "
print(new_str)