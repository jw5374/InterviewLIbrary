def canThreePartsEqualSum(arr: list[int]) -> bool:
    # ==== too slow ====

    # [leftSum, rightSum] = [0, 0]
    # rightEnumeration = {}
    # for i in range(len(arr) - 1, -1, -1):
    #     rightSum += arr[i]
    #     if rightSum in rightEnumeration:
    #         continue
    #     rightEnumeration[rightSum] = i
    # for i in range(len(arr)):
    #     leftSum += arr[i]
    #     num = leftSum
    #     if num in rightEnumeration and (i + 1) < rightEnumeration[num] and sum(arr[i+1:rightEnumeration[num]]) == num:
    #         return True
    # return False
    total = sum(arr)
    if total % 3 != 0:
        return False
    partition = total // 3
    currSum = 0
    res = 0
    for num in arr:
        currSum += num
        if currSum == partition:
            res += 1
            currSum = 0
    return res >= 3
