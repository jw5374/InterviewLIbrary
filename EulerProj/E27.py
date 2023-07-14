import math


def findLongestQuadraticPrime():
    currMax = 0
    coeffs = [0, 0]
    for i in range(-999, 1000):
        for j in range(-1000, 1001):
            sequence = quadraticForm(i, j)
            if currMax < sequence:
                currMax = sequence
                coeffs = [i, j]
    return coeffs


def isPrime(n: int) -> bool:
    if n <= 0 or n == 1:
        return False
    divs = set()
    for num in range(1, math.ceil(math.sqrt(n))):
        if n % num == 0:
            divs.add(num)
            divs.add(n // num)
    return len(divs) == 2


def quadraticForm(a: int, b: int) -> int:
    n = 0
    currNum = math.pow(n, 2) + (n * a) + b
    while isPrime(currNum):
        n += 1
        currNum = math.pow(n, 2) + (n * a) + b
    return n - 1


print(findLongestQuadraticPrime())
