def bubble_sort(nums):
    if_sorted = False
    num_of_loop = 0

    while not if_sorted:
        count = 0
        comp = 0
        for i in range(1, len(nums)-num_of_loop):
            if nums[comp] > nums[i]:
                count = 1
                nums[comp], nums[i] = nums[i], nums[comp]
                comp = i
                continue
            if nums[comp] <= nums[i]:
                comp = i
                continue
        num_of_loop += 1
        if count == 0:
            if_sorted = True
    return nums


def main():
    # print(bubble_sort([5, 3, 8, 2, 1]))
    print(bubble_sort([5, 1, 4, 2, 8]))
    print(bubble_sort([5, 3, 4]))
    print(bubble_sort([1, 2, 3, 4, 5]))


if __name__ == "__main__":
    main()
