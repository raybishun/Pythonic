phrase = "To infinity and beyond..."

# Return only even numbers using 'modulo'
i = 1
while i <= 10:
    if i % 2 == 0:
        print(f'{i}. {phrase}')
    i += 1
print()

# Using 'continue' to return only odd numbers
i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    if i == 7:
        print(f'Found {i}, exiting...')
        break
    print(f'{i}. {phrase}')
    i += 1
print()

# While-else
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print('Done')
print()

# For-else
for i in [1,2,3,4,5]:
    if i == 6:
        print(f'Found :{i}')
        break
else:
    print(f'6 not found.')

print()

# Range
my_range = range(10)
print(my_range)         # Returns range(0, 10)

print(list(my_range))   # Convert range to a list

# Stepping a range
print(list(range(0, 110, 10)))  # Returns 0, 10, 20, ... 100

# _ throwaway variable
for _ in range(10):
    print(f'{_}. hi...')

# -----------------------------------------------------------------------------
# List Comprehensions
# -----------------------------------------------------------------------------
# The normal way...
my_nums = ['one', 'two', 'three', 'four', 'five']
uppercase_my_nums = []
for num in my_nums:
    uppercase_my_nums.append(num.upper())
print(uppercase_my_nums)

# Using List Comprehensions
uppercase_my_nums2 = [num.upper() for num in my_nums]
print(uppercase_my_nums2)

print()

# Using Comprehensions for filtering
# The normal way...
search_results = []
for num in my_nums:
    if num in ['three', 'five', 'seven']:
        search_results.append(num)
print(search_results)

# Using List Comprehensions
search_results2 = [num for num in my_nums if num in ['three', 'five', 'seven']]
print(search_results2)

exit()


for letter in phrase:
    print(letter)

for i in range(1, 11):
    print(f'{i}. {phrase}')
print()

my_list = ['a', 'b', 'c']
for item in my_list:
    print(item)
print()

my_tuple = ('aa', 'bb', 'cc')
for item in my_tuple:
    print(item)
print()

my_dict = {1:'one', 2:'two', 3:'three'}
for k in my_dict:
    print(k)
print()

my_dict = {1:'one', 2:'two', 3:'three'}
for k,v in my_dict.items():
    print(k,v)
print()