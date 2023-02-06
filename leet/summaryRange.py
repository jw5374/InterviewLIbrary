def summaryRanges(nums: list[int]) -> list[str]:
    i = 0
    res = []
    while i < len(nums):
        if i == len(nums) - 1:
            res.append(str(nums[i]))
            break
        j = i + 1
        while j < len(nums):
            if nums[j] != (nums[j-1] + 1):
                break
            j += 1
        if nums[i] == nums[j-1]:
            res.append(str(nums[i]))
        else:
            res.append(f"{nums[i]}->{nums[j-1]}")
        i = j
    return res


print(summaryRanges([0,2,3,4,6,8,9]))

