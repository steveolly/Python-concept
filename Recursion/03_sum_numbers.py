def sum_number(n):
    if n == 0:
        return n
    if n < 0:
        return n + sum_number(n+1)
    else:
        return n + sum_number(n-1)


print(sum_number(4))
print(sum_number(3))
