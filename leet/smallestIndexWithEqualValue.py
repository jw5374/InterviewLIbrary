def smallestEqual(nums: list[int]) -> int:
    for i, val in enumerate(nums):
        if i % 10 == val:
            return i
    return -1


print(smallestEqual([1,2,3,4,5,6,7,8,9,0]))

