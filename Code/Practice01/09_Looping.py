# =============================================================================
# Looping
# =============================================================================

# While Loop
ctr = 1
while ctr <= 10:
    print(ctr) 
    ctr += 1
print()

# For
colors_list = ['blue', 'green', 'red', 'purple']
for color in colors_list:
    print(color)
print()

# For
colors_tuple = ('blue', 'green', 'red', 'purple')
for color in colors_tuple:
    print(color)
print()

# For
ages_dict = {'kevin': 59, 'bob': 40, 'kayla': 21}
for item in ages_dict:
    print(item)
print()

# For
ages_dict = {'kevin': 59, 'bob': 40, 'kayla': 21}
for item in ages_dict.keys():
    print(item)
print()

ages_dict = {'kevin': 59, 'bob': 40, 'kayla': 21}
for item in ages_dict.values():
    print(item)
print()

ages_dict = {'kevin': 59, 'bob': 40, 'kayla': 21}
for k, v in ages_dict.items():
    print(f'{k}\t{v}')
print()

for letter in "Hello World":
    print(letter, end='')
print()

# -----------------------------------------------------------------------------
# Nesting Loops and Conditions
# -----------------------------------------------------------------------------
ctr = 1
i = 1
while ctr <= 48:
    if ctr % 4 == 0:
        print(f'4 x {i} = {ctr}')
        i += 1
    ctr += 1
print()

# -----------------------------------------------------------------------------
# Nesting Loops and Conditions, Controls: Continue
# -----------------------------------------------------------------------------
ctr = 0
while ctr < 10:
    if ctr % 2 == 0:
        ctr += 1
        continue
    print(f"We're counting only odd numbers: {ctr}")
    ctr += 1
print()

# -----------------------------------------------------------------------------
# Nesting Loops and Conditions, Controls: Break
# -----------------------------------------------------------------------------
ctr = 1
while ctr < 10:
    if ctr % 2 == 0:
        break
    print(f"We're counting only odd numbers: {ctr}")
    ctr += 1
print()

colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    if color == 'blue':
        continue
    elif color == 'red':
        break
    print(color)
print()

# -----------------------------------------------------------------------------
# Nesting Loops and Conditions, Controls: Else
# -----------------------------------------------------------------------------
ctr = 1
while ctr <= 4:
    print(ctr)
    ctr += 1
else:
    print("Done.")
print()

for i in [1,2,3,4,5]:
    print(i)
else:
    print("Done.")
print('---')

colors = ['red', 'pink', 'blue', 'orange', 'green']
for color in colors:
    if color == 'orange':
        print('found orange')
    else:
        print("orange not found")
print()


# -----------------------------------------------------------------------------
# Nesting Loops and Conditions, Controls: Range
# -----------------------------------------------------------------------------
print(range(0,10))
print()

print(list(range(0,10)))
print()

print(list(range(0,10,1)))
print()

print(list(range(0,10,2)))
print()

print(list(range(0,10,3)))
print()

count = 1
while count <=4:
    print(f'{count}')
    count += 1
print()

for _ in range(4):
    print("looping")
print()

for i in range(4):
    print(i)
print()

for i in range(0,4):
    print(i)
print()

# -----------------------------------------------------------------------------
# Nesting Loops and Conditions, Controls: List Comprehensions
# -----------------------------------------------------------------------------
colors = ['red', 'blue', 'orange', 'green', 'orange', 'yellow']

uppercase_colors = []

for color in colors:
    uppercase_colors.append(color.upper())

print(uppercase_colors)