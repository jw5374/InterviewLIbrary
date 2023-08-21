def addToArrayForm(num: list[int], k: int) -> list[int]:
    exp = 0
    formedNum = 0
    for i in range(len(num) - 1, -1, -1):
        formedNum += num[i] * (10 ** exp)
        exp += 1
    formedNum += k
    res = []
    while formedNum > 0:
        res = [formedNum % 10] + res
        formedNum //= 10
    return res
