# Control Flow
# =============================================================================
position = False

if(position == True):
    print("Open position...")
elif position == 'Long':
    print("Long...")
elif position == 'Short':
    print("Short...")
else:
    print("Flat...")
print()

# For Loop
# -----------------------------------------------------------------------------
i = 1
prices = ['open', 'high', 'low', 'close', 'vwap', 'pivot']
for price in prices:
    if(price == 'open' or price == 'high' or price == 'low'):
        continue
    if(price == 'vwap'):
        break
    print(f'{i}. {price}')
    i += 1
print()

# Pass
# -----------------------------------------------------------------------------
items = ['a', 'b', 'c']
for item in items:
    # TODO: Please implement next week when you get back from vacation...
    pass
print()

# While Loops
# -----------------------------------------------------------------------------
i = 0
while i < 10:
    i += 1
    if (i == 7):
        print('skip lucky 7')
        continue
    print(i)

print()

# Unpacking Dictionaries
# -----------------------------------------------------------------------------
faang = {'fb': 261.56, 'aapl': 129.87, 'amzn': 3249.90, 'nflx': 540.22, 'goog': 2101.14}
for k in faang:
    print(f'{type(k)}\t{k}')
print()

for k in faang.keys():
    print(f'{type(k)}\t{k}')
print()

for v in faang.values():
    print(f'{type(v)}\t{v}')
print()

for item in faang.items():
        print(f'{type(item)}\t{item}')
print()

for k, v in faang.items():
    print(f'{k}\t{v}')
print()

for (k, v) in faang.items():
    print(f'{k}\t{v}')
print()
print()

# Unpacking Tuples
# -----------------------------------------------------------------------------
faang = [('fb', 261.56, -7.83), ('aapl', 129.87, 0.16), ('amzn', 3249.90, -78.33), ('nflx', 540.22, -8.00), ('goog', 2101.14, -16.06)]
for symbol, close, change in faang:
    print(f'{symbol}\t{close}\t{change}')
print()

# Range, Enumerate and Zip Functions
# =============================================================================
greeting = "Hello World"
my_list = list(greeting)
print(my_list)

for char in list(greeting):
    print(char)

print()

# Range
# -----------------------------------------------------------------------------
for num in range(11):
    print(num)
print()

for num in range(1, 11):
    print(num)
print()

for num in range(1, 11, 2):
    # Print only odd numbers
    print(num)
print()

# Zip
# -----------------------------------------------------------------------------
symbols = ['fb', 'aapl', 'amzn', 'nflx', 'goog']
closes = [261.56, 129.87, 3249.90, 540.22, 2101.14]

# Creates a tuple of each pair
symbols_closes = zip(symbols, closes)

for item in symbols_closes:
    print(item)
print()

for item in zip(symbols, closes):
    print(item)
print()

# Create a list
symbols_closes = list(zip(symbols, closes))
for (symbols, closes) in symbols_closes:
    print(f'{symbols} :: {closes}')
print()

# What happens if the iterables are not the same size?
symbols2 = ['fb', 'aapl', 'amzn', 'nflx', 'goog', 'msft', 'gs', 'ms']
closes2 = [261.56, 129.87, 3249.90, 540.22, 2101.14]
for item in zip(symbols2, closes2):
    print(item)
print()

# Enumerate
# -----------------------------------------------------------------------------
for item in enumerate(symbols):
    print(item)
print()

# Start index at '1'
for item in enumerate(symbols, 1):
    print(item)
print()

# Queries
# -----------------------------------------------------------------------------
symbols = ['fb', 'aapl', 'amzn', 'nflx', 'goog']
print('msft' in symbol) # returns False
print()

# Query by key
print('goog' in {'goog': 2101.14}) # returns True
print()

# Find value
print(2101.14 in {'goog': 2101.14}.values()) # returns True
print()

# Find Min, Max
closes = [261.56, 129.87, 3249.90, 540.22, 2101.14]
print(min(closes))
print(max(closes))
print()

# Random Numbers
# -----------------------------------------------------------------------------
from random import randint
for ny_lotto in range(6):
    print(randint(1, 59))
print()

# Shuffle Numbers
# -----------------------------------------------------------------------------
from random import shuffle
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
shuffle(cards)
print(cards)

my_range = list(range(100, 111))
print(my_range)
shuffle(my_range)
print(my_range)
print()