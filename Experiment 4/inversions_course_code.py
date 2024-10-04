from collections import Counter

def count_inversions(arr):
    """Counts the number of inversions in an array."""
    if len(arr) <= 1:
        return arr, 0  

    mid = len(arr) // 2
    left, left_inversions = count_inversions(arr[:mid])
    right, right_inversions = count_inversions(arr[mid:])

    merged, split_inversions = merge_and_count_split_inversions(left, right)
    return merged, split_inversions + left_inversions + right_inversions

def merge_and_count_split_inversions(left, right):
    """Merges two arrays and counts the number of split inversions."""
    result = []
    i = j = split_inversions = 0    
    n = len(left)                  
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            split_inversions += len(left) - i

    result.extend(left[i:])
    result.extend(right[j:])

    return result, split_inversions


def inversions_course_codes(choices_students):
    """Counts the number of inversions in a list of choices, and classifies them according to the count of inversions."""
    inversions = []
    for choices in choices_students:
        _, t = count_inversions(choices)
        inversions.append(t)
    return Counter(inversions)      # Returns a dictionary with the count of inversions as keys and the number of students with that count as values


choices_students = [
    [101, 102, 103, 104, 105, 106],
    [101, 102, 103, 106, 105, 104],
    [101, 102, 104, 105, 103, 106],
    [101, 102, 104, 103, 105, 106],
    [101, 102, 103, 104, 106, 105],
    [101, 103, 104, 102, 105, 106],
    [101, 102, 104, 106, 103, 105],
    [102, 101, 103, 104, 105, 106],
    [101, 104, 102, 103, 105, 106],
    [101, 102, 104, 103, 106, 105],
]

for k, v in inversions_course_codes(choices_students).items():
    print(f"{v} students have {k} inversion count.")
