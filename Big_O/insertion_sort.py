def insertion_sort(nums: list):
    for i in range(len(nums)-1):
        pointer = i
        for j in range(i+1, 0, -1):
            if nums[j] < nums[pointer]:
                nums[j], nums[pointer] = nums[pointer], nums[j]
                pointer -= 1
            else:
                break
    return nums


def main():
    print(insertion_sort([5, 4, 2, 1, 6, 3]))
    print(insertion_sort([5, 2, 4, 6, 1]))
    print(insertion_sort([5, 4, 3, 2, 1]))


if __name__ == "__main__":
    main()
