# Contitional Statements
# -----------------------------------------------------------------------------
if 'a' < 'b':
    print('true')
    # ...
    # ...
else:
    print('false')
    # ...
    # ...

if True:
    print('true')
elif False:
    print('true by default, never gets here...')

print()

name = input("Enter Password: ")
if name.isalnum():
    print("Valid")
elif name.isspace():
    print("Invalid")
else:
    print("wth...")

print()

# Pass (type of a placeholder)
if name.isnumeric():
    print("isnumeric")
else:
    pass