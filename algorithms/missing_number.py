from utils import generate_sequence


"""

Find the Missing Number in a Sequence

    Description: Given an array of n unique integers where the numbers range from 1 to n+1, find the missing number in the sequence.

    Input: An array arr of integers.

    Output: The missing integer.

    Example:

        Input: [3, 7, 1, 2, 8, 4, 5]
        Output: 6 is missing (1, 2, 3, 4, 5, ?, 7, 8) 

        Input: [3, 7, 1, 2, 8, 4, 5, 6, 12, 9, 11]
        Output: 10

    Complexity: 

        Time: O(n)
        Space: O(1)

"""


def find_missing_number(arr: list) -> int:
    pass


print(find_missing_number([3, 7, 1, 2, 8, 4, 5]))  # 6
print(find_missing_number([3, 7, 1, 2, 8, 4, 5, 6, 12, 9, 11]))  # 10


# Test with large array

# arr = generate_sequence(1000000, 999999)
# print(find_missing_number(arr))  # 999999
