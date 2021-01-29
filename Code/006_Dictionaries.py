# Dictionaries (keys are immutable)
# =============================================================================
ages = { 'parker': 25, 'wayne': 50, 'stark': 40 }
print(ages)

print(ages['parker'])

ages['wayne'] = 51
print(ages)

del ages['parker']
print(ages)

print('banner' in ages)

# Creating dictionaries using the 'dict' key word
avengers = dict(stark=40, parker=25, rogers=500)
print(avengers)

# Creating dictionaries using tuples
league = dict([('wayne', 50), ('kent', 3000)])
print(league)

print()