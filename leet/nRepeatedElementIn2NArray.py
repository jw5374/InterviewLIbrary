def repeatedNTimes(nums: list[int]) -> int:
    numOcc = {}
    target = len(nums) // 2
    for num in nums:
        if num in numOcc:
            numOcc[num] += 1
        else:
            numOcc[num] = 1
    for num, occ in numOcc.items():
        if occ == target:
            return num
