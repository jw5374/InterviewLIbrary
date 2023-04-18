def nextgreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    numsInds = {}
    for i, num in enumerate(nums2):
        numsInds[num] = i
    for i in range(len(nums1)):
        j = numsInds[nums1[i]] + 1
        while j < len(nums2):
            if nums2[j] > nums1[i]:
                nums1[i] = nums2[j]
                break
            j += 1
        else:
            nums1[i] = -1
    return nums1


print(nextgreaterElement([2, 4], [1, 2, 3, 4]))

