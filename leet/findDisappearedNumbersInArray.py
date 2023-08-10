def findDisappearedNumbers(nums: list[int]) -> list[int]:
    setNums = set(nums)
    for i in range(1, len(nums) + 1):
        if i in setNums:
            setNums.remove(i)
        else:
            setNums.add(i)
    return list(setNums)
