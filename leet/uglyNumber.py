import math


def isUgly(n: int) -> bool:
    if n <= 0:
        return False
    if n == 1 or n in {2, 3, 5}:
        return True
    factors = findFactors(n)
    primes = set()
    if len(factors) == 2:
        return False
    for factor in factors:
        if len(findFactors(factor)) == 2:
            primes.add(factor)
    return len(primes.difference(set([2, 3, 5]))) == 0


def findFactors(n: int) -> list[int]:
    if n == 1:
        return [1]
    facs = []
    for i in range(1, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            facs.append(i)
            facs.append(n//i)
    return facs


print(isUgly(28))

