def isMonotonic(nums: list[int]) -> bool:
    if len(nums) == 1:
        return True
    i = 0
    sign = findDiffSign(nums[i], nums[i+1])
    while (i < len(nums) - 1) and sign == 0:
        sign = findDiffSign(nums[i], nums[i+1])
        i += 1
    if i == len(nums) - 1:
        return True
    while i < len(nums) - 1:
        local = findDiffSign(nums[i], nums[i+1])
        if local != 0 and local != sign:
            return False
        i += 1
    return True


def findDiffSign(a, b):
    return (a - b >= 0) - (a - b <= 0)


print(isMonotonic([2, 4, 2, 3]))

