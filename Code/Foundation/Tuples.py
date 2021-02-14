# Tuples (immutable)
# =============================================================================
point = (2.0, 3.0)
point_3d = point + (4.0,)
print(point_3d)

x, y, z = point_3d
print(x)
print(y)
print(z)

print()

kevin = ('Peter Parker', 25, "123-4567")
bruce = ('Bruce Wayne', 50, '')

# list in a tuple
list = [1, 2, 3, 4, 5, 7, 8, 9]
list_in_tuple = (list)
print(list_in_tuple)
print()

# tuple in a list
tuple_in_list = [kevin, bruce]
print(tuple_in_list)

print()