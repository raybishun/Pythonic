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