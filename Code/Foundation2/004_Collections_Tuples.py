# Tuples (immutable)
# =============================================================================
my_tuple = (1, 2, 3, "some data", "some other data", [1, 2, 3])

# TypeError: 'tuple' object does not support item assignment
# my_tuple[3] = "some more data"

print(my_tuple)

# However, since my_tuple contains a list, you can change it's elements
my_tuple[5][1] = 22
print(my_tuple)

print(my_tuple.count("some data"))

# Slicing Tuples
str_tuple = my_tuple[4:5]
print(str_tuple)
print(type(str_tuple))