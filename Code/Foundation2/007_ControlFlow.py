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
    i = i + 1
print()