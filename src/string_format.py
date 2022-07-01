# We simply cannot add an integer to a string. We have to find out a way to
# do it efficiently.

# The string which we are going to work on.
my_age = 18
# main_string = "Hello! I'm Rohan, and I'm " + my_age + " years old."
# would generate:
# Traceback (most recent call last):
#  File "C:\Users\Dr. Rohan\Desktop\code\W3-Python\src\string_format.py", line 6, in <module>
#    main_string = "Hello! What's up? I'm " + my_age + " years old."
# TypeError: can only concatenate str (not "int") to str

main_string = "Hello, I'm Rohan, and I'm {} years old."

print(main_string.format(my_age))

# Multiple variables in formatting.
item_quantity = 5
item_index = 121
item_price = 50.00
item_order_text = "I want to buy {0} copies of item no. {1} for {2} USD."

print(item_order_text.format(item_quantity, item_index, item_price))