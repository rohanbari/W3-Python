# "Variables created outside of a function are global variables."

test_string = 'hello'

def some_function():
    print("Rohan says " + test_string + " in Python!")

some_function()

# Time to use 'global' keyword

def some_other_function():
    global g_str
    g_str = 'mindblowing'

some_other_function()
print("Python is " + g_str)