def divideArray(nums: list[int]) -> bool:
    if len(nums) % 2 != 0:
        return False
    occs = {}
    for num in nums:
        if num in occs:
            occs[num] += 1
        else:
            occs[num] = 1
    for occ in occs.values():
        if occ % 2 != 0:
            return False
    return True
