# Sum Of Odd Elements

print("Sum Of Odd Elements \n")


def sum_of_odd_elements(arr: list) -> int:
    sum = 0

    for i in arr:
        if i % 2 != 0:
            sum += i

    return sum


print(sum_of_odd_elements([1, 2, 3, 4, 5]))  # 9
print(sum_of_odd_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # 25

print("\n*********************************")

# Count Vowels In String

print("Count Vowels In String \n")


def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0

    for i in s:
        if i in vowels:
            count += 1

    return count


def count_vowels_2(s):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    return sum(1 for i in s if i in vowels)


print(count_vowels("hEllo"))  # 2
print(count_vowels("world"))  # 1
print(count_vowels("My name Is ahsen YenIsey"))  # 8

print("\n*********************************")

# Check If Prime Number

print("Check If Prime Number \n")


def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


print(is_prime(29))  # True
print(is_prime(12))  # False

# Special Case
print(is_prime(1000000007))  # True

print("\n*********************************")

# FizzBuzz

print("FizzBuzz \n")


def fizzBuzz(n: int) -> str:
    result = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return ''.join(result)


print(fizzBuzz(3))  # "12Fizz"
print(fizzBuzz(7))  # "12Fizz4BuzzFizz78"
print(fizzBuzz(17))  # "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz1617"

# Sum Of Digits

print("Sum Of Digits \n")


def sum_of_digits(n: int) -> int:
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    return total


print(sum_of_digits(123))  # 6
print(sum_of_digits(12345))  # 15
print(sum_of_digits(123456))  # 21

print("\n*********************************")

# Check Duplicates in Array

print("Check Duplicates in Array \n")


def check_duplicates(arr: list) -> bool:
    duplicates = {}

    for i in arr:
        if i in duplicates:
            return True
        else:
            duplicates[i] = 1

    return False


print(check_duplicates([1, 2, 3, 4, 5]))  # False
print(check_duplicates([1, 2, 3, 4, 1]))  # True
print(check_duplicates([1, 2, 3, 4, 5, 5]))  # True

print("\n*********************************")

# Merge Two Sorted Arrays

print("Merge Two Sorted Arrays \n")


def merge_sorted_arrays(arr1: list, arr2: list) -> list:
    merged = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged


print(merge_sorted_arrays([1, 3, 5], [2, 4, 6, 7, 11]))
# [1, 2, 3, 4, 5, 6, 7, 11]

print(merge_sorted_arrays([3, 4, 5, 7, 15, 45, 50], [1, 2, 3, 8, 12]))
# [1, 2, 3, 3, 4, 5, 7, 8, 12, 15, 45, 50]

print("\n*********************************")

# Find the Maximum Product of Two Elements

print("Find the Maximum Product of Two Elements \n")


def max_product(arr: list) -> int:
    max1 = 0
    max2 = 0

    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

    return max1 * max2


print(max_product([3, 4, 5, 2]))  # 20
print(max_product([3, 7, 1, 9, 8]))  # 72
print(max_product([3, 7, 9, 2]))  # 63
print(max_product([12, 1]))  # 12

print("\n*********************************")


# Find the Missing Number In Sequence

print("Find the Missing Number In Sequence \n")


def find_missing_number(arr: list) -> int:
    n = len(arr) + 1

    current_total = 0
    for num in arr:
        current_total += num

    sequence_total = n * (n + 1) // 2

    return sequence_total - current_total


print(find_missing_number([3, 7, 1, 2, 8, 4, 5]))  # 6
print(find_missing_number([3, 7, 1, 2, 8, 4, 5, 6, 12, 9, 11]))  # 10

print("\n*********************************")

# Reverse a String

print("Reverse a String \n")


def reverse_string(s: str) -> str:
    char_list = list(s)
    l, r = 0, len(char_list) - 1

    while l < r:
        char_list[l], char_list[r] = char_list[r], char_list[l]
        l += 1
        r -= 1

    return ''.join(char_list)


print(reverse_string("hello"))  # "olleh"
print(reverse_string("1234 abc"))  # "cba 4321"

print("\n*********************************")


# Count Frequencies of Characters in a String

print("Count Frequencies of Characters in a String \n")


def count_frequencies(s: str) -> dict:
    frequencies = {}

    for char in s:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1

    return frequencies


print(count_frequencies("hello"))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print(count_frequencies("aabbbc"))  # {'a': 2, 'b': 3, 'c': 1}

print("\n*********************************")
