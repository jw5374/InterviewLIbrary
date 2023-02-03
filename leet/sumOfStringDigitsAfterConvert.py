def getLucky(s: str, k: int) -> int:
    sum = 0
    converted = convertStr(s)
    while k > 0:
        sum = sumDigits(converted)
        converted = sum
        k -= 1
    return sum


def convertStr(s: str) -> int:
    res = ""
    for c in s:
        res += str(ord(c) - 96)
    return int(res)


def sumDigits(n: int) -> int:
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum


print(getLucky("leetcode", 2))

