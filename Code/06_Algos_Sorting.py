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

# -----------------------------------------------------------------------------
# Consumer
# -----------------------------------------------------------------------------
list = [30, 44, 67, 5, 8, 9, 53]
insertionSort(list)
print(list)