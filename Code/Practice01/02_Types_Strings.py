# -----------------------------------------------------------------------------
# Types: Strings
# -----------------------------------------------------------------------------
"""
This is a multi-line string, 
NOT a comment block.
No such thing as a comment block in Python,
use # for comments.
"""

'''
This is also a multi-line string, 
and NOT a comment block.
'''

a_str_literal1 = "Hello World"
print(a_str_literal1)

a_str_literal2 = 'Hello World'
print(a_str_literal2)

print(id(a_str_literal1))
print(id(a_str_literal2))

for char in a_str_literal1:
    # print(char)
    print(char, end='')
print()

# String Concatenation
hello = "Hello "
world = "World"
print(hello + world)

print(hello * 3)

# -----------------------------------------------------------------------------
# Common String Operators
# -----------------------------------------------------------------------------
greeting = "Hello, World!"
lowest_index_as_int = greeting.find(',')
print(lowest_index_as_int)

print(greeting.find('ll'))

print(greeting.lower())
print(greeting.upper())

# -----------------------------------------------------------------------------
# Common Escape Characters
# -----------------------------------------------------------------------------
print("Hello\nWorld")
print("Hello\tWorld")
print("\"Hello World\"")

# -----------------------------------------------------------------------------
# Nested Quotes
# -----------------------------------------------------------------------------
print("'Hello World'")
print('"Hello World"')