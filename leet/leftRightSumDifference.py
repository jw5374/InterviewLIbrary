def leftRightDifference(nums: list[int]) -> list[int]:
    ans = [0] * len(nums)
    for i in range(len(nums)):
        if i == 0:
            ans[i] = sum(nums[i+1:])
            continue
        if i == len(nums) - 1:
            ans[i] = sum(nums[:i])
            continue
        ans[i] = abs(sum(nums[:i]) - sum(nums[i+1:]))
    return ans
