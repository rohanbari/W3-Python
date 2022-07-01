# Strings are nice, but they are nicer when modifiable functions exist.

# The string we are going to experiment on.
main_string = "Hello, world! What's up?"

# Without modification to the actual string, prints it in uppercase.
print(main_string.upper())

# The same as above, but lowercase.
print(main_string.lower())

# Removes any trailing spaces from rear or front end (if any).
print(main_string.strip())

# Replace a string with another string.
print(main_string.replace('Hello', 'Bye'))

# Splitting a string into parts using a delimeter.
print(main_string.split(','))