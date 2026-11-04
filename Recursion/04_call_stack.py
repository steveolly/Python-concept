# import sys
# print(sys.getrecursionlimit())
def count(n):
    print("Entering:", n)

    if n == 0:
        return

    count(n - 1)

    print("Leaving:", n)


count(3)
