"""

Count the Number of 1's in the Binary Representation of a Number

    Description: Given an integer, return the number of 1 bits (also known as the Hamming weight) in its binary representation.

    For example, the binary representation of the integer 11 is 1011, which has three 1s.

    Input: An integer n.

    Output: The number of 1s in the binary representation of n.
    
    Examples:

        Input: 11
        Output: 3
        Explanation: The binary representation of 11 is 1011, which contains three 1s.
    

        Input: 128
        Output: 1
        Explanation: The binary representation of 128 is 10000000.

        Input: 7
        Output: 3

    Complexity:
    
        Time: O(k), where k is the number of 1 bits in n. In the worst case, k can be at most 32 (since n is at most 10^9, which fits in a 32-bit integer).
        Space: O(1)


    Note: Think and research about "Bit Manipulation".
    
"""


def hamming_weight(n: int) -> int:
    pass


print(hamming_weight(11))  # 3
print(hamming_weight(128))  # 1
print(hamming_weight(7))  # 3
