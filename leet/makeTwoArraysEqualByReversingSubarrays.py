def canBeEqual(target: list[int], arr: list[int]) -> bool:
    targetOcc = findOccs(target)
    arrOcc = findOccs(arr)
    for num, occ in arrOcc.items():
        if num not in targetOcc:
            return False
        if num in targetOcc and targetOcc[num] != arrOcc[num]:
            return False
    return True


def findOccs(nums: list[int]) -> dict[int, int]:
    res = {}
    for num in nums:
        if num in res:
            res[num] += 1
        else:
            res[num] = 1
    return res
