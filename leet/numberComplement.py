def findComplement(num: int) -> int:
    num = list(bin(num).split("b")[-1])
    for i, bit in enumerate(num):
        num[i] = str(int(not int(num[i])))
    return int("".join(num), 2)


print(findComplement(5))

