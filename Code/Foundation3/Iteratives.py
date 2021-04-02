phrase = "To infinity and beyond..."

i = 1
while i <= 10:
    print(f'{i}. {phrase}')
    i += 1
print()

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

