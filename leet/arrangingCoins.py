import math


def arrangeCoins(n: int) -> int:
    terms = math.floor(math.sqrt(n*2))
    total = (terms * (terms+1)) // 2
    return terms - 1 if total > n else terms


print(arrangeCoins(8))

