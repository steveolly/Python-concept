def selection_sort(nums):
    current_index = 0

    while current_index < len(nums)-1:
        pointer_index = current_index
        for i in range(current_index, len(nums)):
            if nums[i] < nums[pointer_index]:
                pointer_index = i
        nums[current_index], nums[pointer_index] = nums[pointer_index], nums[current_index]
        current_index += 1

    return nums


def main():
    print(selection_sort([5, 4, 2, 1, 6, 3]))
    print(selection_sort([64, 25, 12, 22, 11]))
    print(selection_sort([5, 5, 5, 5]))
    print(selection_sort([]))
    print(selection_sort([9]))
    print(selection_sort([2, 1]))


if __name__ == "__main__":
    main()
