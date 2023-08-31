def mostFrequentEven(nums: list[int]) -> int:
    evens = [x for x in nums if x % 2 == 0]
    if len(evens) == 0:
        return -1
    freq = {}
    for num in evens:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    res = [-1, 0]
    for num, occ in freq.items():
        if occ > res[1]:
            res = [num, occ]
            continue
        if occ == res[1] and num < res[0]:
            res = [num, occ]
    return res[0]
