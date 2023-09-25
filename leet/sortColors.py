def sortColors(nums: list[int]) -> None:
    occs = {0: 0, 1: 0, 2: 0}
    for num in nums:
        occs[num] += 1
    currNum = 0
    i = 0
    while i < len(nums):
        while occs[currNum] > 0:
            nums[i] = currNum
            occs[currNum] -= 1
            i += 1
        currNum += 1
