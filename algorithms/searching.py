def binary_search(nums, value):
    if len(nums) == 0:
        return None

    midIdx = len(nums) // 2
    mid = nums[midIdx]

    if mid == value:
        return midIdx
    elif mid > value:
        return binary_search(nums[:midIdx], value)
    else:
        return binary_search(nums[midIdx + 1 :], value)
