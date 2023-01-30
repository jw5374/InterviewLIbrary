def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    res = [[],[]]
    hash1 = {}
    hash2 = {}
    for num in set(nums1):
        if num not in hash1:
            hash1[num] = True
    for num in set(nums2):
        if num in hash1:
            del hash1[num]
            continue
        if num not in hash2:
            hash2[num] = True
    for num in hash1.keys():
        res[0].append(num)
    for num in hash2.keys():
        res[1].append(num)
    return res


print(findDifference([1,2,3,3], [1,1,2]))

