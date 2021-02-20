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