# Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}

s = {8, 7, 12, "Harry", [1,2]}

# set cannot contain a list in Python.
# Because sets can only contain immutable (hashable) objects, and lists are mutable, so they are unhashable and cannot be elements of a set.
