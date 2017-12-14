"""
In your class, you have started lessons about arithmetic progression.
Since you are also a programmer, you have decided to write a function that will
return the first 'n' elements of the sequence with the given common difference 'r' and first element 'a'.
Result should be separated by comma and space.

Example:

arithmetic_sequence_elements(1, 2, 5) == '1, 3, 5, 7, 9'
"""


def arithmetic_sequence_elements(a, r, n):
    return ', '.join([str((a + ((n-1) * r))) for n in range(1, n+1)])
