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