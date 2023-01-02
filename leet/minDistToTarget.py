def getMinDistance(nums: list[int], target: int, start: int) -> int:
    [left, right] = [start, start]
    while nums[left] != target and nums[right] != target:
        if left > 0:
            left -= 1
        if right < len(nums) - 1:
            right += 1
    leftDist = abs(start - left)
    rightDist = abs(right - start)
    return leftDist if nums[left] == target else rightDist


print(getMinDistance([1,1,1,1,1,1,1,1], 1, 0))

