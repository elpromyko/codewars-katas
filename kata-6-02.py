"""
Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether
the two arrays have the "same" elements, with the same multiplicities.
Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

"""


def comp(array1, array2):
    try:
        return sorted([i*i for i in array1]) == sorted(array2)
    except TypeError:
        return False
