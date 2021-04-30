# Introduction to Algorithms

### Algorithms are used to:
* Identify solutions to common problems
* Understand the efficiency of solutions to common problems
* Evaluate and break-down problems into distinct parts

### All algorithms must:
* Produce a result (output)

### Search Algorithms Types
* Linear Search
* Binary Search

### Linear Search
* Every item in the collection is checked, regardless if sorted or not

### Binary Search
* Requires a sorted collection
* Continuously split in the middle, and ask a comparison question

### Complexity
* Time Complexity - measures the time it takes for an algorithm to run
* Space Complexity - measures the storage used by an algorithm

### Constant and Logarithmic Time
* Constant Time, O(1) - where n is irrelevant; it doesn't matter if n is 1 or 1M - the algorithm takes the same amount of time to execute

* Logarithmic Time, O(log n) - as the data set increases, the algorithm's execution time increases logarithmically

### Linear and Quadratic Time
* Linear Time, O(n) - the algorithm's runtime is directly proportional to the data set's size

* Quadratic Time - O(n^2) - the algorithm's runtime increases by a factor of n squared as the data set's size increases

### Common Complexity Review 
* Big O - where the 'O' means 'Order of magnitude', NOT complexity!
* O(1) - means, 1 or 1,000 - completes in the same amount of time (constant time)
* O(n) - linear time, meaning runtime increases, as the data set increases

### Quasilinear Time
* Quasilinear Time, O(n log n) - for a data set of size n, an algorithm executes n number of operations where each operation runs in log n (logarithmic) time
* Used in Sorting alorithms, i.e., Merge Sorts