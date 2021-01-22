# Strings
# -----------------------------------------------------------------------------
myStr = 'my string'
print(f'{myStr}', f'{id(myStr)}')

# this actually creates a NEW string
myStr = myStr.capitalize() 
print(f'{myStr}', f'{id(myStr)}')

print()


# Immutability of Strings
# -----------------------------------------------------------------------------

# Here the 2 variables are pointing to the same memory location

myStr = "Ray"
print(f'{myStr}', f'{id(myStr)}')

myOtherStr = "Ray"
print(f'{myOtherStr}', f'{id(myOtherStr)}')

print()

# .len(string)
# -----------------------------------------------------------------------------
myStr = "Hello World"
print(len(myStr))

print()