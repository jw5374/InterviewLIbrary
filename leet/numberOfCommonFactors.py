import math


def commonFactors(a: int, b: int) -> int:
    factors = 0
    lesser = a if a <= b else b
    for num in range(1, math.floor(math.sqrt(lesser)) + 1):
        if a % num == 0 and b % num == 0:
            factors += 1
        if a % (lesser // num) == 0 and b % (lesser // num) == 0 and (lesser//num) != num:
            factors += 1
    return factors
