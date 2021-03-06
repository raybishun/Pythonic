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

# Continue
# -----------------------------------------------------------------------------
i = 1
print('Even numbers between 1 and 10:')
while i <= 10:
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i += 1

print()

# Break
# -----------------------------------------------------------------------------
i = 1
print('Even numbers between 1 and 10:')
while i <= 10:
    print(i)
    if i % 2 != 0:
        break
    print(f'Exited at {i}.')
    i += 1

print()

# Break and Continue
# -----------------------------------------------------------------------------
symbols = ('FB', 'MSFT', 'AMZN', 'AAPL', 'NFLX', 'GOOG')
for symbol in symbols:
    if symbol == 'FB':
        continue
    elif symbol == 'AMZN':
        break
    print(symbol)

print()

# Practical use of Break and Else
# -----------------------------------------------------------------------------
symbols = ('FB', 'MSFT', 'AMZN', 'AAPL', 'NFLX', 'GOOG')
for symbol in symbols:
    if symbol == 'GOOG':
        print(f'Found {symbol}!')
        break
else:
    print(f'GOOG Not found')

print()

# Range (are immutable)
# -----------------------------------------------------------------------------
my_range = range(13)
print(my_range)
print(list(my_range))

print()

my_range = list(range(1, 13, 2)) # where the step is 2 in this case
print(my_range)

print()

for _ in my_range:
    print(f'{_}.')

print()

# List Comprehensions
# -----------------------------------------------------------------------------
symbols = ('fb', 'msft', 'amzn', 'aapl', 'nflx', 'goog')

# Silly way :)
print(f'Lower: {symbols}')
uppercase_symbols = []
for symbol in symbols:
    uppercase_symbols.append(symbol.upper())
print(f'Upper: {uppercase_symbols}')

print()

# Using  List Comprehensions
uppercase_symbols2 = [symbol.upper() for symbol in symbols]
print(uppercase_symbols2)

print()

only_faang = []
for symbol in symbols:
    if symbol in ['fb', 'amzn', 'aapl', 'nflx', 'goog']:
        only_faang.append(symbol)
print(only_faang)
print()

only_faang2 =[symbol for symbol in symbols if symbol in ['fb', 'amzn', 'aapl', 'nflx', 'goog']]
print(only_faang2)