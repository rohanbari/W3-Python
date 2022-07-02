# Many times, only a yes/no is the best solution.

# Testing values
op1 = 10
op2 = 9

# Basic boolean operators used in comparison.
print(op1 > op2)
print(op1 < op2)
print(op1 == op2)

# Python can evaluate any values to produce either True or False.
print(bool("Welcome"))
print(bool(18))
print(bool('0'))

# Empty strings, sets, and the described below are evaluated False.
print(bool(""))
print(bool(()))
print(bool({}))
print(bool([]))
print(bool(0))

# Implementing a class for the first time!
# If a class object has __len__ 0, it is evaluated False.
class TestClass():
    def __len__(self):
        return 0

object = TestClass()
print(bool(object))

# isinstance() tells whether the first argument is a type of second argument.
print(isinstance(op1, int))
print(isinstance(op1, bool))