# =============================================================================
# Dictionaries {}
# =============================================================================
dc_universe = {'peter.parker': 'Spiderman'}

dc_universe['bruce.wayne'] = 'Batman'

dc_universe['clark.kent'] = "Superman"

del dc_universe['bruce.wayne']

print(dc_universe)
print()

print('clark.kent' in dc_universe)

print('bruce.wayne' in dc_universe)

# -----------------------------------------------------------------------------
# Creating a dictionary using dict()
# -----------------------------------------------------------------------------
marvel_universe = dict(stark='Ironman', rogers='Captain America')
print(marvel_universe)
print()

# -----------------------------------------------------------------------------
# Creating a dictionary using tuples
# -----------------------------------------------------------------------------
villains = dict([('bad.guy1', 'Joker'), ('bad.guy2', 'Riddler')])
print(villains)
print()

# -----------------------------------------------------------------------------
# Dictionary Methods
# -----------------------------------------------------------------------------

# keys(), retuns a list
print(marvel_universe.keys())
print()

# values(), retuns a list
print(marvel_universe.values())
print()

# items(), retuns a tuple
print(marvel_universe.items())
print()
