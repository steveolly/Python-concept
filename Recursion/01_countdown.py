def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n-1)
    print(n*2)
    print(f"finished {n}")


countdown(5)
