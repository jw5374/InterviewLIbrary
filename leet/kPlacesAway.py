def kLengthApart(nums: list[int], k: int) -> bool:
    spaceApart = 0
    i = 0
    while i < len(nums) - 1:
        if nums[i]:
            i += 1
            while i < len(nums) - 1 and not nums[i]:
                i += 1
                spaceApart += 1
            if i == len(nums) - 1 and not nums[i]:
                return True
            if spaceApart < k:
                return False
            spaceApart = 0
        else:
            i += 1
    return True


print(kLengthApart([1, 0, 0, 0, 1, 0, 0, 1, 0], 2))

