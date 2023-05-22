import math
import timeit


def isThree(n: int) -> bool:
    divs = set()
    for i in range(1, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
        if len(divs) > 3:
            return False
    return len(divs) == 3


def isThreePrimeCheck(n: int) -> bool:
    if n == 1:
        return False
    root = math.floor(math.sqrt(n))
    if root ** 2 != n:
        return False
    for i in range(2, math.floor(math.sqrt(root)) + 1):
        if root % i == 0:
            return False
    return True


def isThreeRegularLoop() -> None:
    for i in range(1, 10001):
        isThree(i)


def isThreePrimeLoop() -> None:
    for i in range(1, 10001):
        isThreePrimeCheck(i)


numsHash = {}
for i in range(1, 10001):
    if isThree(i):
        numsHash[i] = 1
    if isThreePrimeCheck(i):
        numsHash[i] = 2
print(numsHash)


regularTime = timeit.repeat(stmt=isThreeRegularLoop, repeat=5, number=100)
primeTime = timeit.repeat(stmt=isThreePrimeLoop, repeat=5, number=100)
print(f"Regular check: {regularTime}")
print(f"Prime check: {primeTime}")

