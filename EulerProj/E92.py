def findDigitChains():
    res = 0
    for i in range(1, 10000001):
        curr = i
        while curr != 1 and curr != 89:
            curr = sumDigitSquares(curr)
        if curr == 89:
            res += 1
    return res


def sumDigitSquares(num: int) -> int:
    res = 0
    while num > 0:
        res += (num % 10) ** 2
        num //= 10
    return res


print(findDigitChains())

