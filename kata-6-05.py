"""
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example

sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

"""


def sort_array(source_array):
    odd_numbers = []
    n = 0
    for num in source_array:
        if num % 2 != 0:
            odd_numbers.append(num)
            source_array[source_array.index(num)] = ' '
    odd_numbers.sort()
    for place in source_array:
        if place == ' ':
            source_array[source_array.index(place)] = odd_numbers[n]
            n += 1
    return source_array
