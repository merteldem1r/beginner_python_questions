"""

FizzBuzz

    Description: Write a program that prints the numbers from 1 to n. However, for multiples of 3, print "Fizz" instead of the number, and for the multiples of 5, print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz".

    Input: An integer n.

    Output: A string where each character corresponds to either the number itself or one of "Fizz", "Buzz", or "FizzBuzz" based on the rules, concatenated together without space.

    Examples:

        Input: 3
        Output: "12Fizz"

        Input: 7
        Output: "12Fizz4BuzzFizz7" 

        Input: n = 17
        Output: "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz1617"

    Complexity: 

        Time: O(n)
        Space: O(n)

    Note: Think and research about mutable and immutable strings
        
"""


def fizzBuzz(n: int) -> str:
    pass


print(fizzBuzz(3))  # "12Fizz"
print(fizzBuzz(7))  # "12Fizz4BuzzFizz78"
print(fizzBuzz(17))  # "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz1617"

# Test with large number

# print(fizzBuzz(12673357))
