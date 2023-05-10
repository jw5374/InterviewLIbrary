def evenOddBit(n: int) -> list[int]:
    bits = bin(n).split("b")[-1]
    res = [0, 0]
    for i in range(len(bits)-1, -1, -2):
        if bits[i] == "1":
            res[0] += 1
        if i > 0 and bits[i-1] == "1":
            res[1] += 1
    return res
