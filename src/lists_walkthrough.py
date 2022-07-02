# Welcome to the beginning of Lists. It allows duplicates.

fruits_inventory = ['apple', 'banana', 'cherry', 'dates', 'cherry']
print(fruits_inventory)

print("The length of the list is " + str(len(fruits_inventory)))

# Jinx: A list may contain different data types.
evergreen_list = ["John Wick", 27, 525000.50, 104, 'male']

print(evergreen_list)
print(type(evergreen_list))

# Using list() constructor when creating a new list.
ctor_list = list(('volvo', 'bugatti', 'ferrari'))
print(ctor_list)