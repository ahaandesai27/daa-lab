def linear_search(arr, element):
    """Performs a linear search for the element in the array."""
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1

def binary_search(arr, element, start, end):
    """Performs a binary search for the element in the array, using recursion."""
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == element:
        return mid
    elif arr[mid] > element:
        return binary_search(arr, element, start, mid - 1)
    else:
        return binary_search(arr, element, mid + 1, end)

def linear_search_test():
    """Run test cases for the linear search function."""
    testcases = [
        # (array, element, expected_output)
        ([1, 5, 4, 2, 3], 4, 2),
        ([10, 7, 15, 203, 51], 16, -1),
        ([20, 25, 31, 400, 65], 25, 1),
        ([1, 9, -1, -2, -100, -61], -2, 3),
        ([-105, 66, 111, 215, 330], -60, -1),
    ]
    print("Linear Search tests:")
    for i, (array, element, expected_output) in enumerate(testcases):
        print(f"Test {i + 1} - ", end="")
        output = linear_search(array, element)
        if output == expected_output == -1:
            print("Element not found")
        elif output == expected_output:
            print(f"Element found at index {expected_output}")
        else:
            print("Test failed!")

def binary_search_test():
    """Run test cases for the binary search function."""
    testcases = [
        # (array, element, expected_output)
        ([6, 7, 8, 9, 10], 9, 3),
        ([100, 102, 104, 110, 115], 115, 4),
        ([21, 23, 24, 25, 28], 23, 1),
        ([52, 56, 57, 58, 60, 62], 55, -1),
        ([-4, -3, -2, -1, 0], -5, -1)
    ]
    print("Binary Search tests:")
    for idx, (array, element, expected_output) in enumerate(testcases):
        print(f"Test {idx + 1} - ", end="")
        output = binary_search(array, element, 0, len(array) - 1)
        if output == expected_output == -1:
            print("Element not found")
        elif output == expected_output:
            print(f"Element found at index {expected_output}")
        else:
            print("Test failed!")

# Call tests
linear_search_test()
binary_search_test()
