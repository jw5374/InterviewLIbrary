def areNumbersAscending(s: str) -> bool:
    nums = [int(x) for x in s.split(" ") if x.isdigit()]
    curNum = -1
    for num in nums:
        if curNum >= num:
            return False
        curNum = num
    return True
