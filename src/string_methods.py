# We can do so many things with strings that we cannot imagine.
# Let's try some of them...
# 
# Please refer to the link below to know about the methods in-depth.
#   <https://www.w3schools.com/python/python_strings_methods.asp>
# 

main_string = "Hello, world! I'm Rohan Bari, 18 y/o."

# Only the first letter shall be capitalized. Rest of them becomes lowercase.
print(main_string.capitalize())

# Lowercases a string, same effects as of lowercase() function.
print(main_string.casefold())

# Returns a centered string, where the max chars is passed as args.
print(main_string.center(50))

# This function will count the occurrence of the number of a phrase in a string.
print(main_string.count('a'))

# Returns the raw bytes of string.
print(main_string.encode())

# It checks whether the string ends with the specified value.
print(main_string.endswith('old'))

# ... so many string functions ...

# Returns the index where the specified phrase is found.
print(main_string.index('Bari'))

# Partitions a string by:
#   - before the specified phrase occurs
#   - when it occurs
#   - after it occurs
# as a tuple.
print(main_string.partition('I\'m'))

print('\nFor more reference, please visit:')
print('https://www.w3schools.com/python/python_strings_methods.asp')