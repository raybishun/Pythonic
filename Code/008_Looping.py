# While Loop
# =============================================================================
i = 0
while(i < 10):
    i = i + 1
    print(i)

print()

# For Loops
# =============================================================================

# Looping through a string
# -----------------------------------------------------------------------------
symbol = 'Google' 
for letter in symbol:
    print(letter)

print()

# Looping through an array
# -----------------------------------------------------------------------------
symbols = ['FB', 'AMZN', 'AAPL', 'NFLX', 'GOOG']
symbols[4] = 'MSFT'
for symbol in symbols:
    print(symbol)

print()

# Looping through a tuple
# -----------------------------------------------------------------------------
symbols = ('FB', 'AMZN', 'AAPL', 'NFLX', 'GOOG')
#symbols[4] = 'MSFT' # No can do, since this is a tuple
for symbol in symbols:
    print(symbol)

print()

# Looping through a dictionary
# -----------------------------------------------------------------------------
symbols = {'FB': 268.10, 'AMZN': 3352.15, 'AAPL': 136.76, 'NFLX': 550.79, 'GOOG': 2098.00}
for key, value in symbols.items():
    print(f'{key}\t{value}')

print()

# Nesting Loops and Conditionals
# -----------------------------------------------------------------------------
i = 1
print('Even numbers between 1 and 10:')
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1

print()