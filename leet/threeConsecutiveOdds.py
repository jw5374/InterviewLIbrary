def threeConsecutiveOdds(self, arr: list[int]) -> bool:
    odds = 0
    for num in arr:
        if num % 2 == 0:
            odds = 0
        else:
            odds += 1
            if odds == 3:
                return True
    return False
