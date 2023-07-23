def targetIndices(nums: list[int], target: int) -> list[int]:
    nums.sort()
    targetInd = binarySearch(nums, target)
    if targetInd == -1:
        return []
    [i, j] = [targetInd, targetInd]
    while (-1 < i - 1) and nums[i - 1] == target:
        i -= 1
    while (len(nums) > j + 1) and nums[j + 1] == target:
        j += 1
    return [x for x in range(i, j+1)]


def binarySearch(nums: list[int], target: int) -> int:
    [left, right] = [0, len(nums) - 1]
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1
