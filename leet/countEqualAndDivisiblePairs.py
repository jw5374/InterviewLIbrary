def countPairs(nums: list[int], k: int) -> int:
    freqs = {}
    res = 0
    for i, num in enumerate(nums):
        if num in freqs:
            freqs[num].append(i)
        else:
            freqs[num] = [i]
    for num, inds in freqs.items():
        if len(inds) < 2:
            continue
        res += findDivPairs(inds, k)
    return res


def findDivPairs(indices: list[int], k: int) -> int:
    numPairs = 0
    for i in range(len(indices)-1):
        for j in range(i+1, len(indices)):
            if (indices[i] * indices[j]) % k == 0:
                numPairs += 1
    return numPairs


print(countPairs([1,2,3,4], 1))

