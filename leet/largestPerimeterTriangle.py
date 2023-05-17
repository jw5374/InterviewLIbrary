def largestPerimeter(nums: list[int]) -> int:
    nums.sort()
    for i in range(len(nums) - 1, 1, -1):
        sides = [nums[i], nums[i-1], nums[i-2]]
        if checkTriangle(sides):
            return sum(sides)
    return 0


def checkTriangle(sides: list[int]) -> bool:
    a = (sides[0] + sides[1]) > sides[2]
    b = (sides[0] + sides[2]) > sides[1]
    c = (sides[1] + sides[2]) > sides[0]
    return a and b and c
