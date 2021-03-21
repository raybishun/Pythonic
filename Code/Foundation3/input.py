# input
golden_ratio = float(input("Golden Ratio: ") or 1.618)
print(f'{type(golden_ratio)}\t{golden_ratio}')

# change the end-of-line
print("one", "two", end=" ")
print("three")

# change separator
print("out", "of", "office")
print("out", "of", "office", sep="-")