def maxProduct(nums: list[int]) -> int:
    nums.sort()
    return (nums[-1]-1)*(nums[-2]-1)

print(maxProduct([1,5,4,5]))

