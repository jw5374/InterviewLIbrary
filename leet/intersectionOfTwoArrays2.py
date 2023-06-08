def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    numOccs = {}
    res = []
    for num in nums1:
        if num in numOccs:
            numOccs[num] += 1
        else:
            numOccs[num] = 1
    for num in nums2:
        if num in numOccs and numOccs[num] > 0:
            res.append(num)
            numOccs[num] -= 1
    return res
