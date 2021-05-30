# =============================================================================
# Lists []
# =============================================================================
my_list = [1,2,3,4,5,'six',7,"eight",9,10]
print(my_list)
print(my_list[5])
print(len(my_list))
print(my_list[::])
print(my_list[:7:])
print(my_list[::2]) # 1, 3, 5, 7, 9
my_list[0] = "apple"
print(my_list[::])
my_list += ["a", "b", 'c'] # in this case, += actually creates a new list
print(my_list)
my_list[10:13] = ['d', 'e', 'f']
print(my_list)

# The del 'statement'
del my_list[2] # delete the '3'
print(my_list)
print()

# =============================================================================
# List Methods and List Functions
# =============================================================================

# -----------------------------------------------------------------------------
# Methods
# -----------------------------------------------------------------------------
# append
my_list = [1,2,3]
my_list.append(4)
print(my_list)
print()

# insert
my_list.insert(1, "I'm at index one")
print(my_list)
print()

# index
print(my_list.index("I'm at index one"))
print()

# in
print(3 in my_list)
print(3 not in my_list)
print()

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------

# sorted
my_list = [1, 3, 8, 2, 7, 4, 9, 6, 5]
my_list_sorted = sorted(my_list)
print(my_list_sorted)
print()

# reversed
my_list_reversed = list(reversed(my_list_sorted))
print(my_list_reversed)
print()

# -----------------------------------------------------------------------------
# Nested Lists (Matrices and Cubes)
# -----------------------------------------------------------------------------

"""
A type of matrix would be a Cube = same number of columns as rows, i.e., 3 x 3 or 5 x 5
"""
my_matrix = [
    [1,2,3],
    [4,5,6]
]

print(my_matrix)
print()

print(len(my_matrix))
print()

print(f'Row: {len(my_matrix[0])}')
print(f'Row: {len(my_matrix[1])}')
print()

# rc
print(my_matrix[1][1]) # 5
print()