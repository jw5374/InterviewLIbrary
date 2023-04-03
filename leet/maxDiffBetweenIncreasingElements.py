def maximiumDifference(nums: list[int]) -> int:
    currMax = nums.pop()
    maxDiff = -1
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] < currMax:
            maxDiff = max(maxDiff, currMax - nums[i])
        else:
            currMax = nums[i]
    return maxDiff


print(maximiumDifference([342,423,364,564,675,675,254,214,563,756,345,25,234,532,344,56,645,313,53,646,523,132,3,121,12,575,8,97,5,65,235,5,354,64,767,68,789]))

