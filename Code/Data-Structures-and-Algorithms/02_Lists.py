my_list = [1,2,3]
print(my_list)
print()

my_list2 = [ [1,2,3], ['a', 'b', 'c'], [4,5,6] ]
print(my_list2)
print()

print(my_list2[0][2])   # 3
print(my_list2[2])      # [4,5,6]
print(my_list2[1][1])   # b
print()

items = ['a','b','c']
print(items)

items.append('d')
print(items)

items.insert(1, 'msft')
print(items)

items.extend('apple')
print(items)