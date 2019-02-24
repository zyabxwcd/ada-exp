# Function to maintain max-heap property
def max_heapify(data, n, i):
    largest = i
    l = 2 * i + 1 # Left child position
    r = 2 * i + 2 # Right child position
 
    # Compare left child and root
    if l < n and data[i] < data[l]:
        largest = l
 
    # Compare right child and root
    if r < n and data[largest] < data[r]:
        largest = r
 
    # Change root, if needed, that is if it’s not the largest
    if largest != i:
        # Swap current root and largest
        data[i],data[largest] = data[largest],data[i]
 
        # Heapify the root
        max_heapify(data, n, largest)
 

# The main function to sort an array
def heap_sort(data):
    n = len(data)
 
    # Building a maxheap
    for i in range(n, -1, -1):
        max_heapify(data, n, i)
 
    # Extracting elements one at a time
    for i in range(n-1, 0, -1):
        data[i], data[0] = data[0], data[i]
        max_heapify(data, i, 0)
  
  
num = [int(i) for i in input().split()]
print('Input number list:', num)

heap_sort(num)

print('After heap sort:', num)
