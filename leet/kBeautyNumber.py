import math


def divisorSubstrings(num: int, k: int) -> int:
    divs = findDivisors(num)
    numStr = str(num)
    beauty = 0
    for i in range(len(numStr) - (k-1)):
        if int(numStr[i:i+k]) in divs:
            beauty += 1
    return beauty


def findDivisors(num: int) -> dict[int, int]:
    res = {}
    for i in range(1, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            res[i] = 1
            res[num // i] = 1
    return res


print(divisorSubstrings(30003, 3))

