'''
Implementing Quick Sort in Python 3.
Output:
Enter unsorted array: 3 2 1 7 9 -1
Pass 1: Pivot element is 1. Array: [-1, 1, 2, 7, 9, 3]
Pass 2: Pivot element is -1. Array: [-1, 1, 2, 7, 9, 3]
Pass 3: Pivot element is 7. Array: [-1, 1, 2, 3, 9, 7]
Pass 4: Pivot element is 2. Array: [-1, 1, 2, 3, 9, 7]
Pass 5: Pivot element is 9. Array: [-1, 1, 2, 3, 7, 9]
Sorted Array: [-1, 1, 2, 3, 7, 9]
'''

# Global variable for showing iterations
counter = 0

def quick_sort(arr):
    _quick_sort(arr, 0, len(arr) - 1)

def _quick_sort(arr, left ,right):
    global counter

    if left >= right:
        return
    
    # Increment iteration counter
    counter += 1

    # Taking pivot as the element in middle
    pivot = arr[(left + right) // 2]
    index = partition(arr, left, right, pivot)

    print(f'Pass {counter}: Pivot element is {pivot}. Array: {arr}')
    
    # Recursively apply quick sort on left and right sub-arrays
    _quick_sort(arr, left, index - 1)
    _quick_sort(arr, index, right)

def partition(arr, left, right, pivot):
    while left <= right:
        # Break on finding an element bigger than pivot in LHS
        while arr[left] < pivot:
            left += 1

        # Break on finding an element smaller than pivot in RHS
        while arr[right] > pivot:
            right -= 1

        # Swap the unordered elements on LHS & RHS
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    # Return index of the dividing element
    return left

arr = [int(i) for i in input('Enter unsorted array: ').split()]
quick_sort(arr)
counter = 0
print('Sorted Array:', arr)