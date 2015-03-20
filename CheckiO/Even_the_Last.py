# Challenge:

# You are given an array of integers.
# You should find the sum of the elements with even indexes (0th, 2nd, 4th...)
# then multiply this summed number and the final element of the array together.
# Don't forget that the first element has an index of 0.
# For an empty array, the result will always be 0 (zero).
# Input: A list of integers.
# Output: The number as an integer.
# Precondition: 0 ≤ len(array) ≤ 20
# all(isinstance(x, int) for x in array)
# all(-100 < x < 100 for x in array)

# My Solution:


def checkio(array):
    x = len(array)
    y = []
    z = 0
    if x == 0:
        return 0
    else:
        for i in range(0, x, 2):
            if i % 2 == 0:
                y.append(array[i])
                z += array[i]
        return z * array[-1]