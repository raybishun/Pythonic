# Typecasting
# -----------------------------------------------------------------------------
print(float(1))

# Note, this is not rounding; the floating point portion is trucated
print(int(1.618)) 

print(str(1)) # returns '1'

print(int('1'))

# Interesting this error is returned:
# --> Exception has occurred: ValueError: invalid literal for int() with base 10: '1.618'
# print(int('1.618')) 

print()

# Input Function (with type casting)
# -----------------------------------------------------------------------------
fname = str(input("Enter first name: "))
lname = str(input('Enter last name: '))
age = int(input('Age: '))
print()

# Print using positional arguments
# -----------------------------------------------------------------------------
# Print on a new line
print(fname)
print(lname)
print()

# Print on the same line
print(fname, end=" ")
print(lname)
print()

# Print using SEP (note, space is the default separator)
print(fname, lname, sep=" - ")
print()

# Print Function with String Interpolation
# -----------------------------------------------------------------------------
print(f'{lname}, ' f'{fname}', f'{age}')
print()