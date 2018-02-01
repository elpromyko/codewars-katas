"""
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example

sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

"""


def sort_array(source_array):
    odd_numbers = iter(sorted([i for i in source_array if i % 2]))
    return [next(odd_numbers) if i % 2 else i for i in source_array]
