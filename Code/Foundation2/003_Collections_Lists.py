# Collection Data Types: Lists (a mutable type), aka arrays
# =============================================================================
my_list = [1, 2, 3, 4, 15, 6, 17, 8]
my_list.pop() # remove last element
what_was_removed = my_list.pop(2) # removes 3 from list
print(what_was_removed) # pop() retuns int
my_list.reverse()
print(my_list)
my_list.sort()
my_list[2] = "GOOG"
my_list.append(['fb', 'msft', 'aapl'])
print(my_list)
print(type(my_list))

# Using slicing with Lists
print(my_list[-1])
print(my_list[6:])
print(len(my_list))

# List Concatenation
my_list2 = ['a', 'b', 'c', 'msft']
new_list = my_list + my_list2
print(new_list)

# Querying nested lists
print(my_list[6]) # return the nested array
print(my_list[6][1]) # return the 2nd element in the nested array

# Get Index
print(my_list.index('GOOG'))

# Count occurance
print(my_list2)
print(my_list2.count('msft'))