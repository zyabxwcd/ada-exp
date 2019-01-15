def insertionSort(test_cases):
    sorted = []

    for test_case in test_cases:
        print("Test Case :", test_case)

        for i in range(1, len(test_case)):
            key = test_case[i]
            j = i - 1

            while(j >= 0 and test_case[j] >= key):
                test_case[j+1] = test_case[j]
                j = j - 1

            test_case[j+1] = key
            print("Pass", i, ":", test_case)

        sorted.append(test_case)

    return sorted


test_cases = [[2, 1, 4, 3],
              [1, 2, 3, 4],
              [4, 3, 2, 1]]
print("Sorted Array :", insertionSort(test_cases))
