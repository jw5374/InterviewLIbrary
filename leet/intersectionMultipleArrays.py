def intersection(nums: list[list[int]]) -> list[int]:
    occurrences = {}
    res = []
    for num in nums.pop():
        occurrences[num] = 1
    for arr in nums:
        for num in arr:
            if num in occurrences:
                occurrences[num] += 1
    for key, val in occurrences.items():
        if val == (len(nums) + 1):
            res.append(key)
    res.sort()
    return res


print(intersection([[1,2,3],[4,5,6]]))

