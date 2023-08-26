def mostFrequent(nums: list[int], key: int) -> int:
    occs = {}
    for i in range(len(nums) - 1):
        if nums[i] != key:
            continue
        if nums[i + 1] in occs:
            occs[nums[i + 1]] += 1
        else:
            occs[nums[i + 1]] = 1
    resTarget = [0, 0]
    for target, occ in occs.items():
        if resTarget[1] < occ:
            resTarget = [target, occ]
    return resTarget[0]
