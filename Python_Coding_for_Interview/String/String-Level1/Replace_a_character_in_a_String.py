# Write a python program that prints the string s with the character current_charcter replaced by the character new_character
#Method-1

# s="World"
# print(s.replace("W","A"))

#Method-2

s="Hello"
new_s=""
curr_char="l"
new_char="s"

for i in s:
    if i==curr_char:
        new_s+=new_char
    else:
        new_s+=i
print(new_s)