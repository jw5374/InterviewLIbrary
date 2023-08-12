def sortArrayByParityII(nums: list[int]) -> list[int]:
    indexStack = []
    for i, val in enumerate(nums):
        if i % 2 == 0 and val % 2 == 0:
            continue
        if i % 2 != 0 and val % 2 != 0:
            continue
        if len(indexStack) == 0:
            indexStack.append(i)
            continue
        if (indexStack[-1] % 2 == 0 and i % 2 != 0) or (indexStack[-1] % 2 != 0 and i % 2 == 0):
            swapIndex = indexStack.pop()
            nums[i], nums[swapIndex] = nums[swapIndex], nums[i]
            continue
        indexStack.append(i)
    return nums
