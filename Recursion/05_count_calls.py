def count_calls(n):
    if n == 0:
        return
    print(f"Calling {n}")
    count_calls(n-1)
    print(f"Returning {n}")


count_calls(4)
