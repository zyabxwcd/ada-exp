def mergeSort(alist):
    # Base case is if number of elements is 1
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        print('Divided Arrays:', lefthalf, '+', righthalf)

        # Recursively mergesort divided sub-arrays
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0  # Pointer for Left-half
        j = 0  # Pointer for Right-half
        k = 0  # Pointer for Sorted array

        # Compare and add corresponding elements
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i+1
            else:
                alist[k] = righthalf[j]
                j = j+1
            k = k+1

        # Add remaining elements
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1

        # Add remaining elements
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j+1
            k = k+1

        print('Merged Array:', alist)


# Test Cases
alist = [[2, 1, 3, 4],
         [1, 2, 3, 4],
         [4, 3, 2, 1]]

for test_case in alist:
    print('Input:', test_case)
    mergeSort(test_case)
    print('Sorted Array:', test_case, '\n')
