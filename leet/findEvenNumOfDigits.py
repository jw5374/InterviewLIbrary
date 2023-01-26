def findNumbers(nums: list[int]) -> int:
    res = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            res += 1
    return res


print(findNumbers([555,901,482,1771]))

