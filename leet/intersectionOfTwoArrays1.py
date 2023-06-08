def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    numHash = {}
    res = []
    for num in nums1:
        numHash[num] = True
    for num in nums2:
        if num in numHash:
            res.append(num)
            del numHash[num]
    return res
