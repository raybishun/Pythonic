"""
- This is a multi-line string object!!!
- Not a comment block!!!
"""

'''
- This is also a multi-line string object!!!
- Not a comment block!!!
'''

# Use of single quotes ('...') with a string literal
greeting1 = 'Hello, World!'

# Use of double quotes ("...") with a string literal
greeting2 = "Hello, World!"

# Python is not strongly typed
greeting1 = 1.618

print(greeting1)
print(greeting2)

print(greeting1)

index = greeting2.find(',')
print(index)

# Scientific Notation
scientific_notation = 4.5e9
x = 4.5 * (10 ** 9)
print(scientific_notation == x)
