# =============================================================================
# Tuples (immutable type)
# =============================================================================
my_tuple = (1,2,3)
print(my_tuple)
print()

# umpacking a tuple
x,y,z = my_tuple
print(z)
print()

also_a_tuple = (1,)
print(also_a_tuple)
print()

# =============================================================================
# Tuples vs Lists
# =============================================================================

# Tuples could be used to model an object
peter_parker = ('Peter Parker', 'Spiderman')
bruce_wayne = ('Bruce Wayne', 'Bruce Wayne')
print(peter_parker[1])
print()

# Imbedding lists in tuples or vice versa

# Lists within Tuples can be modified
