def totalMoney(n: int) -> int:
    weekBase = (n // 7) * 28
    extraMoney = sum(list(range(1, n // 7))) * 7
    remaining = sum(list(range((n // 7) + 1, (n // 7) + (n % 7) + 1)))
    return weekBase + extraMoney + remaining


print(totalMoney(4))

