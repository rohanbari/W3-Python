# Slicing the strings in Python

# The string on which we are going to work.
main_string = "Hello, World! What's up?"

# Printing from 2nd to the 5(-1)th position (llo)
print(main_string[2:5])

# Slice from the start (Hello)
print(main_string[:5])

# Slice from 2nd position to the end (llo, World! What's up?)
print(main_string[2:])

# Negative indexed slices
print(main_string[-5:-2])