def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    valInds = {}
    for i, num in enumerate(nums):
        if num in valInds and (i - valInds[num]) <= k:
            return True
        valInds[num] = i
    return False


print(containsNearbyDuplicate([1,2,3,1], 3))

