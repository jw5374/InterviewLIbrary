def findMiddleIndex(nums: list[int]) -> int:
    sums = findLeftRightSums(nums)
    for i in range(len(sums[0])):
        if sums[0][i] == sums[1][i]:
            return i
    return -1


def findLeftRightSums(nums: list[int]) -> list[list[int]]:
    left = [0] * len(nums)
    right = [0] * len(nums)
    for i in range(1, len(nums)):
        left[i] += left[i-1] + nums[i-1]
    for i in range(len(nums) - 2, -1, -1):
        right[i] += right[i+1] + nums[i+1]
    return [left, right]
