def frequencySort(nums: list[int]) -> list[int]:
    freqs = {}
    for num in nums:
        if num in freqs:
            freqs[num] += 1
        else:
            freqs[num] = 1
    listItems = []
    for num, freq in freqs.items():
        listItems.append([num, freq])
    listItems.sort(key=lambda x: x[0], reverse=True)
    listItems.sort(key=lambda x: x[1])
    res = []
    for listNums in [[x[0]] * x[1] for x in listItems]:
        res += listNums
    return res
