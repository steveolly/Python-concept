numbers = [10, 20, 30, 40, 50, 60, 70, 80]
target = 100
left = 0
right = len(numbers)-1


while left <= right:
    mid = (left+right)//2
    if numbers[mid] == target:
        print(f"Target is in index {mid}")
        break
    elif numbers[mid] > target:
        right = mid - 1
    elif numbers[mid] < target:
        left = mid + 1
else:
    print("No target")
