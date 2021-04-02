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

