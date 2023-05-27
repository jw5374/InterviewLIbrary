def countElements(nums: list[int]) -> int:
    [minimum, maximum] = [nums[0], nums[0]]
    res = 0
    for num in nums:
        minimum = min(num, minimum)
        maximum = max(num, maximum)
    for num in nums:
        res += 1 if num != minimum and num != maximum else 0
    return res
