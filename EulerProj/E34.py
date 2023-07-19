import math
from typing import List

factorials = [0] * 10

for i in range(0, 10):
    factorials[i] = math.factorial(i)


def splitDigits(num: int) -> List[int]:
    res = []
    while num > 0:
        res.append(num % 10)
        num //= 10
    return res


def findDigitSumFactorials():
    totalSum = 0
    for i in range(3, 10000000):
        digits = splitDigits(i)
        factorialSum = 0
        for digit in digits:
            factorialSum += factorials[digit]
        if factorialSum == i:
            print(i)
            totalSum += i
    return totalSum


print(findDigitSumFactorials())
