def decompressRLElist(nums: list[int]) -> list[int]:
    i = 0
    res = []
    while (2 * i + 1) < len(nums):
        sub = [nums[i * 2 + 1]] * nums[i * 2]
        res += sub
        i += 1
    return res
