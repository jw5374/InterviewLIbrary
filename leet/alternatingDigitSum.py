import math


def alternatingDigitSum(n: int) -> int:
    flag = 1 if math.floor(math.log10(n)) % 2 == 0 else -1
    res = 0
    while n > 0:
        res += (n % 10) * flag
        flag *= -1
        n //= 10
    return res


print(alternatingDigitSum(886996))

