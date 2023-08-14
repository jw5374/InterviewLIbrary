import sys
sys.set_int_max_str_digits(1000000)


def addStrings(num1: str, num2: str) -> str:
    [a, b] = [0, 0]
    exp = 0
    for i in range(len(num1) - 1, -1, -1):
        a += (ord(num1[i]) - 48) * (10 ** exp)
        exp += 1
    exp = 0
    for i in range(len(num2) - 1, -1, -1):
        b += (ord(num2[i]) - 48) * (10 ** exp)
        exp += 1
    return str(a + b)
