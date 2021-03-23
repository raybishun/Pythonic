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

del mylist                          # deletes the entire list!!!
# print(my_list)                    # returns "my_list is not defined"

# =============================================================================
# Sets
# =============================================================================
# my_list = [1, 2, 2, 3, 4, 5, 5]
# uniques = set(my_list)
# print(uniques)

# another_set = {'a', 'b', 'c', 'c', 'd'}
# print(type(another_set))

# another_set.add(1.168)
# another_set.remove('b')
# print(another_set)