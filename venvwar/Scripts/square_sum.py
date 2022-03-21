"""
Complete the square sum function so that it squares each number passed into 
it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

"""


def square_sum(numbers):
    nl = []
    list_sum = 0
    for n in numbers:
        n = n ** 2
        nl.append(n)
    for number in nl:
        list_sum += number

    return list_sum
