def findKDistantIndices(nums: list[int], key: int, k: int) -> list[int]:
    res = set()
    for i, val in enumerate(nums):
        if val == key:
            low = i - k if i - k >= 0 else 0
            high = i + k + 1 if i + k + 1 < len(nums) else len(nums)
            res.update(range(low, high))
    return list(res)


print(findKDistantIndices([2,2,2,2,2], 2, 2))

