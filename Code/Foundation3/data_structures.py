# =============================================================================
# Sets
# =============================================================================
my_list = [1, 2, 2, 3, 4, 5, 5]
uniques = set(my_list)
print(uniques)

another_set = {'a', 'b', 'c', 'c', 'd'}
print(type(another_set))

another_set.add(1.168)
another_set.remove('b')
print(another_set)