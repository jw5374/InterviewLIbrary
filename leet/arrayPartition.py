def arrayPairSum(nums: list[int]) -> int:
    nums.sort()
    sum = 0
    for i in range(len(nums) - 2, -1, -2):
        sum += nums[i]
    return sum
