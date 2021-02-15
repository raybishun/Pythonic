# Collection Data Types: Dictionaries, (mutable) key-vale pairs, 
# Note: Dictionaries are not sorted
# =============================================================================
dict = {'the_key': 'the value', 9: [1, 2, 3], 'isValid': True, 
    'a_list': [4, False, 'five', {'a_dict_in_a_list_within_a_dict': 'why...'}],
    'tuple': (618, 1.618)}
print(dict)
print(dict['the_key'])
print(dict[9])
dict[9] = 1.618
print(dict)
what_was_removed = dict.pop(9)
print(what_was_removed)

# Add an item to a Dictionary
dict['spiderman'] = 'peter.parker'
print(dict)

print(dict['a_list'][1])

print(dict['a_list'][3]['a_dict_in_a_list_within_a_dict'])

print(dict['tuple'][1])

# Clear
# dict.clear()
# print(dict)