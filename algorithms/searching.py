def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i


def binary_search(nums, target):
    if len(nums) == 0:
        return None

    midIdx = len(nums) // 2
    mid = nums[midIdx]

    if mid == target:
        return midIdx
    elif mid > target:
        return binary_search(nums[:midIdx], target)
    else:
        return binary_search(nums[midIdx + 1 :], target)
