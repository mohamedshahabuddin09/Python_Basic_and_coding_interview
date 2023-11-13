# Write a python program that adds a new key-value pair to a dictionary only if the key does not exist already
# If the key-value pair exists in the dictionary,do not update the existing value. the dictionary should not be modified in this case
# Store the new key in the new_key variable and the new value in the new_value variable
# Print the final value of the dictionary

my_dictionary={"January":45,"February":56,"March":67}
new_key="April"
new_value=87

if new_key not in my_dictionary:
    my_dictionary[new_key]=new_value
print(my_dictionary)