def mystery(n):
    if n == 0:
        return 0

    print("Before:", n)
    result = mystery(n - 1)
    print("After:", n)

    return result + n


print("Result:", mystery(3))
