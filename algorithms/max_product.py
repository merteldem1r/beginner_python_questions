from utils import generate_random_array


"""

Find the Maximum Product of Two Elements

    Description: Given an array of integers, find the maximum product of any two distinct elements in the array.

    Input: An array arr of integers.

    Output: An integer representing the maximum product of two elements in the array.

    Example:

        Input: [1, 5, 4, 5]
        Output: 25 (5 * 5)

        Input: [3, 7, 1, 9, 8]
        Output: 72 (9 * 8)

    Complexity:

        Time: O(n) 
        Space: O(1)

        
"""


def max_product(arr: list) -> int:
    pass


print(max_product([3, 4, 5, 2]))  # 20
print(max_product([3, 7, 1, 9, 8]))  # 72
print(max_product([3, 7, 9, 2]))  # 63
print(max_product([12, 1]))  # 12

# Test with large array

# arr = generate_random_array(1000000)
# print(max_product(arr))
