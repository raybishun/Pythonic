# Lists[]
# -----------------------------------------------------------------------------
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums)

anything = [1, 'apple', True, 1.618]
print(anything)

print(len(anything))
print(anything[3])

# Return odd numbers (using Stepping)
print(nums[0:9:2])

# Return the first 2 elements (using Slicing)
print(anything[0:2])

# Modify list
nums[2] = 33
print(nums)

# Append to list
nums += [10, 11, 12]
print(nums)

# Replace elements
nums[0:2] = [11, 22]
print(nums)

# Remove elements (the last 3 in this example)
nums[9:] = []
print(nums)

# The del statement (to remove the 0-3 elements in this example)
del nums[0:3]
print(nums)

print()

#A few list members
# -----------------------------------------------------------------------------
myList = [1, 2, 3, 'really', False, 99, 1.618, "ok"]
myList.append(4)
print(myList)

myList.insert(0, 'I inserted this')
print(myList)

goldenRatioPosition = myList.index(1.618)
print(goldenRatioPosition)

print(1.618 in myList)
print(100 not in myList)

anotherList = [5, 4, 6, 300, 95, 2]
print(sorted(anotherList))

reversedList = list(reversed(anotherList))
print(reversedList)

print()