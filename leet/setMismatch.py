def findErrorNums(nums: list[int]) -> list[int]:
    occs = {}
    res = [0, 0]
    for num in nums:
        if num in occs:
            occs[num] += 1
        else:
            occs[num] = 1
    for key, val in occs.items():
        if val > 1:
            res[0] = key
            break
    for i in range(1, len(nums) + 1):
        if i not in occs:
            res[1] = i
            return res


print(findErrorNums([3,2,3,4,6,5]))

