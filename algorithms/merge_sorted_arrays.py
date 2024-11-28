"""

Merge Two Sorted Arrays

    Description: You are given two sorted arrays, arr1 and arr2, which may have different lengths. Write a function to merge these two arrays into one sorted array. The merged array should also be sorted in non-decreasing order.

    Input:

        arr1: A sorted list of integers.
        arr2: Another sorted list of integers.

    Output: A single list that merges arr1 and arr2 in sorted order.

    A single list that merges arr1 and arr2 in sorted order.

    Examples:

        Input: arr1 = [1, 3, 5] arr2 = [2, 4, 6, 7, 11]
        Output: [1, 2, 3, 4, 5, 6, 7, 11]

        Input: arr1 = [1, 2, 3, 8, 12] arr2 = [3, 4, 5, 7, 15]
        Output: [1, 2, 3, 3, 4, 5, 7, 8, 12, 15]

    Complexity:

        Time: O(m + n)
        Space: O(m + n)
        
"""


def merge_sorted_arrays(arr1: list, arr2: list) -> list:
    pass


print(merge_sorted_arrays([1, 3, 5], [2, 4, 6, 7, 11]))
# [1, 2, 3, 4, 5, 6, 7, 11]

print(merge_sorted_arrays([3, 4, 5, 7, 15, 45, 50], [1, 2, 3, 8, 12]))
# [1, 2, 3, 3, 4, 5, 7, 8, 12, 15, 45, 50]
