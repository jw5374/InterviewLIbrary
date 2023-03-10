def sumOddLengthSubarrays(arr: list[int]) -> int:
    res = 0
    for i in range(len(arr)):
        [left, right] = [i, i]
        while left >= 0 and right < len(arr):
            res += sum(arr[left:right+1])
            left -= 1
            right += 1
    return res


print(sumOddLengthSubarrays([10,11,12]))

