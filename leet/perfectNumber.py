import math

def checkPerfectNumber(num: int) -> bool:
    if num == 1:
        return False
    return sum(findDivisors(num)) == num


def findDivisors(num: int) -> list[int]:
    res = [1]
    for i in range(2, math.floor(math.sqrt(num)+1)):
        if num % i == 0:
            res.append(i)
            res.append(num // i)
    return res


print(checkPerfectNumber(6))

