# Typecasting
# -----------------------------------------------------------------------------
print(float(1))

# Note, this is not rounding; the floating point portion is trucated
print(int(1.618)) 

print(str(1)) # returns '1'

print(int('1'))

# Interesting this error is returned:
# --> Exception has occurred: ValueError: invalid literal for int() with base 10: '1.618'
print(int('1.618')) 