def binaryGap(n: int) -> int:
    num = bin(n).split("b")[-1]
    print(num)
    i = 0
    res = 0
    while i < len(num):
        currInd = 0
        if num[i] == "1":
            print(i)
            currInd = i
            i += 1
            while i < len(num) and num[i] != "1":
                print(num[i], i)
                i += 1
        if i < len(num) and num[i] == "1":
            res = max(res, (i - currInd))
    return res


print(binaryGap(7862786))

