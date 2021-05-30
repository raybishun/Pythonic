hi = "Hello world"
print(hi.istitle())

# You can actually chain methods
print(hi.title().istitle())
print()

print(" ".isspace())
print(' '.isspace())
print()

# -----------------------------------------------------------------------------
# Weird number methods
# -----------------------------------------------------------------------------
print('1.0'.isdecimal())    # Actually retuns false
print('1'.isdecimal())      # True
print()

print('1.0'.isdigit())      # Actually retuns false
print('1'.isdigit())        # True
print()

print('1.0'.isnumeric())    # Actually retuns false
print('1'.isnumeric())      # True
print()

# -----------------------------------------------------------------------------
# Alpha-numeric methods
# -----------------------------------------------------------------------------
print('abc'.isalpha())
print('abc123'.isalpha())
print()

print('abc'.isalnum())      # Actually returns true
print('abc123'.isalnum())   # True
print()

# -----------------------------------------------------------------------------
# Check if an identifier can be used as a variable name
# -----------------------------------------------------------------------------
print('1abc'.isidentifier())    # False
print('abc.def'.isidentifier()) # False
print()

# -----------------------------------------------------------------------------
# Check if printable
# -----------------------------------------------------------------------------
print('Hello there...'.isprintable())       # True
print('Hello there...\n'.isprintable())     # False
print()

# -----------------------------------------------------------------------------
# String Methods Part 2..........
# -----------------------------------------------------------------------------

# split
greeting = "Buy low sell high"
words = greeting.split(' ')

for word in words:
    print(word)

print()

last_word = greeting.split(' ')[-1]
print(last_word)
print()

# join
print("; ".join(words))
print("\n".join(words))
print()

my_thank_you_template = "Hello {}, thank for meeting with me on {}."
print(my_thank_you_template.format("Ray", "Monday"))
print()

my_thank_you_template = "Hello {1}, thank for meeting with me on {0}."
print(my_thank_you_template.format("Ray", "Monday"))

