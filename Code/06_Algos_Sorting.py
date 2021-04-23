# -----------------------------------------------------------------------------
# Algorithms: Sorting: Insertion Sort
# -----------------------------------------------------------------------------
def insertionSort(list):
    for i in range(1, len(list)):
        value = list[i]
        j = i
        while(j > 0 and list[j - 1] > value):
            list[j] = list[j - 1]
            j = j - 1
    
        list[j] = value

# Insertion Sort Consumer
list = [30, 44, 67, 5, 8, 9, 53]
insertionSort(list)
print(list)
print()

# -----------------------------------------------------------------------------
# Algorithms: Sorting: Selection Sort
# -----------------------------------------------------------------------------
def selectionSort(list):
    for i in range(0, len(list) -1):
        minValueIndex = i
        for j in range(i + 1, len(list)):
            if(list[minValueIndex] > list[j]):
                minValueIndex = j

        tempValue = list[i]
        list[i] = list[minValueIndex]
        list[minValueIndex] = tempValue

# Selection Sort Consumer
list = [30, 44, 67, 5, 8, 9, 53]
selectionSort(list)
print(list)
print()