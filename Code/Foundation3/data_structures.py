# -----------------------------------------------------------------------------
# Lists
# -----------------------------------------------------------------------------
my_list = [1, 2, 2, 3, 4, 5, 5]
print(len(my_list))
print(my_list[0:4])
my_list[1] = 11                     # mutable
print(my_list)
another_list = ['six', 7, 'eight']  # not statically typed
my_list += another_list
print(my_list)

# del statement (not a function!!!)
del my_list[7]                      # delete the 7th element from the list
print(my_list)

del my_list                         # deletes the entire list!!!
# print(my_list)                    # returns "my_list is not defined"
print()

my_list = [1, 2, 9, 3, 6, 5, 8, 7]
my_list.append(4)
print(my_list)

my_list.insert(2, 'after # 2')
print(my_list)

print(f'1 is found at index: {my_list.index(1)}')

# True/False
print(3 in my_list)
print(3 not in my_list)

my_list =  [1, 2, 9, 3, 6, 5, 8, 7]
sorted_list = sorted(my_list)
print(sorted_list)

# Simply reverses the original list
print(list(reversed(my_list)))
print()


# -----------------------------------------------------------------------------
# Sets
# -----------------------------------------------------------------------------
# my_list = [1, 2, 2, 3, 4, 5, 5]
# uniques = set(my_list)
# print(uniques)

# another_set = {'a', 'b', 'c', 'c', 'd'}
# print(type(another_set))

# another_set.add(1.168)
# another_set.remove('b')
# print(another_set)

# -----------------------------------------------------------------------------
# Matrices/Cubes (lists within lists)
# -----------------------------------------------------------------------------
# Matrices
my_matrix = [[1,2,3], 
            [3,5,6]]
print(my_matrix)

row_count = len(my_matrix)
print(row_count)        # 2

column_count = len(my_matrix[0])
print(column_count)     # 3

print(my_matrix[0][2])  # 3
print(my_matrix[1][2])  # 6

# Cubes (same columns as rows, not just 3s)
my_cube = [ [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
            [[19, 20, 21], [22, 23, 24], [25, 26, 27]]]

print(my_cube)
print(my_cube[1][1][0]) # 13
print()

# -----------------------------------------------------------------------------
# Tuples
# -----------------------------------------------------------------------------
# Immutable
# Created using () and at least 1 ,
point = (2.0, 3.0)
print(point)

# Append to a tuple, however, you're creating another tuple
new_point = point + (4.0,)
print(new_point)
print()

# Unpacking a tuple
a, b, c, = new_point
print(a)
print(b)
print(c)
print()

# Tuples in Lists, and vice versa
# (a list within a tuple can be changed), but tuples are immutable
my_list = [1,2,3]
my_tuple = (my_list, 4, 5, 6)
print(my_list)
print(my_tuple)
print()

my_list2 = [7,8,9, my_tuple]
print(my_list2)
print()