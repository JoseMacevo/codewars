def reverse_seq(n):
    numbers = [i for i in range(1, n+1)]
    reverse_nums = numbers[::-1]
    return reverse_nums


print(reverse_seq(5))

