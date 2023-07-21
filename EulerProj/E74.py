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


def findDigitFactorialChains():
    res = 0
    for i in range(1, 1000001):
        curr = i
        visited = set()
        while curr > 1:
            digits = splitDigits(curr)
            factorialSum = 0
            for digit in digits:
                factorialSum += factorials[digit]
            if factorialSum in visited:
                break
            visited.add(factorialSum)
            curr = factorialSum

        # 60 if counting the final repeat element
        if len(visited) == 59:
            res += 1
            print(i)
    return res


print(findDigitFactorialChains())
